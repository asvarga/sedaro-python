import gzip
import json
from pathlib import Path
from typing import Generator, Union

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, HFILL, hfill


class SedaroBlockResult:

    def __init__(self, structure, series: dict):
        '''Initialize a new block result.

        Block results are typically created through the .block method of
        SedaroAgentResult or the .from_file method of this class.
        '''
        if 'name' in structure:
            self.__name = structure['name']
        elif structure == 'root':
            self.__name = 'root'
        else:
            self.__name = '<Unnamed Block>'
        self.__structure = structure
        self.__series = series
        self.__variables = [variable for data in self.__series.values() for variable in data['series']]

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        for module in self.__series:
            if name in self.__series[module]['series']:
                return SedaroSeries(
                    name,
                    self.__series[module]['time'],
                    self.__series[module]['series'][name],
                )
        else:
            raise ValueError(f'Variable "{name}" not found.')

    def __contains__(self, variable: str) -> bool:
        '''Check if this block contains a variable by name.'''
        return variable in self.variables

    def __iter__(self) -> Generator:
        '''Iterate through variables on this block.'''
        return (self.__getattr__(variable) for variable in self.variables)

    def __repr__(self) -> str:
        return f'SedaroBlockResult({self.name})'

    @property
    def name(self):
        return self.__name

    @property
    def modules(self):
        return self.__series.keys()

    @property
    def variables(self):
        return self.__variables

    def module_to_dataframe(self):
        raise NotImplementedError("")

    def variable(self, name: str) -> SedaroSeries:
        '''Query a particular variable by name.'''
        return self.__getattr__(name)

    def to_file(self, filename: Union[str, Path], verbose=True) -> None:
        '''Save agent result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'structure': self.__structure, 'series': self.__series}
            json.dump(contents, json_file)
            if verbose:
                print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load agent result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['structure'], contents['series'])

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print("Sedaro Simulation Block Result Summary".center(HFILL))
        if self.name != '<Unnamed Block>':
            print(f"'{self.name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.modules:
            print(f'    • {ENGINE_EXPANSION[module]}')

        print("\n📋 Variables Available")
        for variable in self.variables:
            print(f'    • {variable}')
        hfill()
        print("❓ Query variables with .<VARIABLE_NAME>")
        print("📊 Display all block variables statistics with .stats( output_html=False ) ")

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}


    def scatter_matrix(self):
        try:
            import pandas as pd
            from pandas.plotting import scatter_matrix
            import matplotlib.pyplot as plt
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            var_dfs = []

            def add_to_df_list(first_value, column_name, data):
                if type(first_value) is list:
                    list_len = len(first_value)
                    columns = [f'{column_name}_X', f'{column_name}_Y', f'{column_name}_Z']
                    if list_len == 4:
                        columns.append(f'{column_name}_Q') 
                    var_dfs.append( pd.DataFrame(data, columns=columns ) )
                else:
                    var_dfs.append( pd.DataFrame(data, columns=[column_name]) )

            for variable_name in self.variables:
                variable_data = self.variable(variable_name)                
                column_name = f'{self.name}.{variable_name}'
                if variable_data.has_subseries:
                    for key, subtype in variable_data.subtypes:
                        first_value = variable_data[key].values[0]
                        data = variable_data[key].values
                        add_to_df_list(first_value, f'{column_name}.{key}', data)
                        break
                else:
                    first_value = variable_data.values[0]
                    data = variable_data.values
                    add_to_df_list(first_value, column_name, data)
                    
            block_dfs = pd.concat( var_dfs, axis=1)
            just_numbers = block_dfs.select_dtypes(include=['number'])
            no_distint_cols = just_numbers[[c for c in list(just_numbers)
                                                    if len(just_numbers[c].unique()) > 1]]
            sm = scatter_matrix(no_distint_cols, alpha=0.2, figsize=(12,12), diagonal='kde')
            # Change label rotation
            [s.xaxis.label.set_rotation(90) for s in sm.reshape(-1)]
            [s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]
            [s.get_yaxis().set_label_coords(-2.0,0.5) for s in sm.reshape(-1)]
            [s.set_xticks(()) for s in sm.reshape(-1)]
            [s.set_yticks(()) for s in sm.reshape(-1)]
            plt.show()
        except ImportError:
            raise ValueError('Statistics is disabled because pandas could not be imported. (pip install pandas)')

    def stats(self, output_html=False):
        try:
            import pandas as pd
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            var_dfs = []

            def add_to_df_list(first_value, column_name, data):
                if type(first_value) is list:
                    list_len = len(first_value)
                    columns = [f'{column_name}_X', f'{column_name}_Y', f'{column_name}_Z']
                    if list_len == 4:
                        columns.append(f'{column_name}_Q') 
                    var_dfs.append( pd.DataFrame(data, columns=columns ) )
                else:
                    var_dfs.append( pd.DataFrame(data, columns=[column_name]) )

            for variable_name in self.variables:
                variable_data = self.variable(variable_name)
                        
                column_name = f'{self.name}.{variable_name}'
                if variable_data.has_subseries:
                    for key, subtype in variable_data.subtypes:
                        first_value = variable_data[key].values[0]
                        data = variable_data[key].values
                        add_to_df_list(first_value, f'{column_name}.{key}', data)
                else:
                    first_value = variable_data.values[0]
                    data = variable_data.values
                    add_to_df_list(first_value, column_name, data)
            block_dfs = pd.concat( var_dfs, axis=1)
            try:
                from IPython.display import display
                display(block_dfs.describe(include='all').T)
            except:
                print(block_dfs.describe(include='all').T)

        except ImportError:
            raise ValueError('Statistics is disabled because pandas could not be imported. (pip install pandas)')

        try:
            import sweetviz as sv
        except ImportError:
            print( "Histogram plots require the sweetviz library to be imported. (pip import sweetviz)")
        else:
            sv.config_parser['Layout']['show_logo'] = '0' 
            sv_report = sv.analyze(block_dfs, pairwise_analysis="off" )

            if output_html:
                sv_report.show_html(filepath=f'Block_{self.name}_Report.html')
            else:
                sv_report.show_notebook(w="90%", h="full", layout='vertical')
