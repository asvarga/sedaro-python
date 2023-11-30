import gzip
import json
from functools import cached_property

from scipy.interpolate import interp1d

try:
    import matplotlib.pyplot as plt
except ImportError:
    PLOTTING_ENABLED = False
else:
    PLOTTING_ENABLED = True


from .utils import HFILL, _get_series_type, bsearch, hfill


class SedaroSeries:

    def __init__(self, name, time, series):
        '''Initialize a new time series.

        Series are typically created through the .<VARIABLE_NAME> attribute or
        .variable method of SedaroBlockResult or the .from_file method of
        this class.
        '''
        self.__name = name
        self.__mjd = time
        self.__elapsed_time = [86400 * (entry - self.__mjd[0]) for entry in self.__mjd]
        self.__series = series
        self.__has_subseries = isinstance(self.__series, dict)
        if self.__has_subseries:
            self.__dtype = {key: _get_series_type(subseries) for key, subseries in self.__series.items()}
        else:
            self.__dtype = _get_series_type(series)

    def __repr__(self):
        return f"Series({self.name})"

    def __iter__(self):
        '''Iterate through time, value pairs in this series.

        Only a series with no subseries is iterable.
        '''
        if self.__has_subseries:
            raise ValueError('Select a specific subseries to iterate over.')
        return (entry for entry in zip(self.__mjd, self.__elapsed_time, self.__series))

    def __len__(self) -> int:
        return len(self.mjd)

    def __getitem__(self, subseries_name: str):
        '''Get a particular subseries by name.

        Typically invoked by indexing [<SUBSERIES_NAME>] on an instance
        of SedaroSeries. Can only be called if the series has subseries.
        '''
        if not self.__has_subseries:
            raise ValueError('This series has no subseries.')
        elif subseries_name in self.__series:
            new_series_name = f'{self.__name}.{subseries_name}'
            return SedaroSeries(new_series_name, self.__mjd, self.__series[subseries_name])
        else:
            raise ValueError(f"Subseries '{subseries_name}' not found.")

    def __getattr__(self, subseries_name: str):
        '''Get a particular subseries by name as an attribute.'''
        return self[subseries_name]

    @property
    def has_subseries(self):
        return self.__has_subseries

    @property
    def name(self):
        return self.__name

    @property
    def elapsed_time(self):
        return self.__elapsed_time

    @property
    def mjd(self):
        return self.__mjd

    @property
    def values(self):
        return self.__series

    @property
    def subtypes(self):
        if self.has_subseries:
            return self.__dtype.items()
        else:
            return {}


    @cached_property
    def values_interpolant(self):
        return interp1d(self.__mjd, self.__series)

    @property
    def duration(self):
        return (self.mjd[-1] - self.mjd[0]) * 86400

    def value_at(self, mjd, interpolate=False):
        '''Get the value of this series at a particular time in mjd.'''
        if self.__has_subseries:
            return {key: self.__getattr__(key).value_at(mjd, interpolate=interpolate) for key in self.__dtype}
        else:
            def raise_error():
                raise ValueError(f"MJD {mjd} not found in series with bounds [{self.__mjd[0]}, {self.__mjd[-1]}].")
            if mjd < self.__mjd[0] or mjd > self.__mjd[-1]:
                raise_error()
            if not interpolate:
                index = bsearch(self.__mjd, mjd)
                if index < 0:
                    raise_error()
            else:
                return self.values_interpolant(mjd)
            return self.__series[index]

    def plot(self, show=True, ylabel=None, elapsed_time=True, height=None, xlim=None, ylim=None, **kwargs):
        self.__plot(show, ylabel, elapsed_time, height, xlim, ylim, **kwargs)

    # def scatter(self, **kwargs):
    #     # TODO: Does not work with 2D value arrays
    #     show = kwargs.pop('show', True)
    #     self.__plot(plt.scatter, show, kwargs)

    def __plot(self, show, ylabel, elapsed_time, height, xlim, ylim, **kwargs):
        if not PLOTTING_ENABLED:
            raise ValueError('Plotting is disabled because matplotlib could not be imported.')
        if self.__has_subseries:
            raise ValueError('Select a specific subseries to plot.')
        try:
            if height is not None:
                plt.rcParams['figure.figsize'] = [plt.rcParams['figure.figsize'][0], height]
            plt.plot((self.__elapsed_time if elapsed_time else self.__mjd), self.__series, **kwargs)
            if 'label' in kwargs:
                plt.legend(loc='upper left')
            plt.xlabel('Elapsed Time (s)' if elapsed_time else 'Time (MJD)')
            plt.ylabel(ylabel)
            if xlim:
                plt.xlim(xlim)
            if ylim:
                plt.ylim(ylim)
            if show:
                plt.show()
        except Exception:
            raise ValueError(
                "The data type of this series does not support plotting or the keyword arguments passed were unrecognized.")

    def stats(self, output_html=False):
        if self.__has_subseries:
            raise ValueError('Select a specific subseries to generate statitics.')
            # for key, value in self.__dtype.items():
            #     if value == 'None':
            #         print(f"    - '{key}': All entries in this subseries are None")
            #     else:
            #         print(f"    - '{key}': '{value}'")
            #         self.__series[key].stats(output_html)

        try:
            import pandas as pd
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
        except ImportError:
            STATS_ENABLED = False
        else:
            STATS_ENABLED = True

        if not STATS_ENABLED:
            raise ValueError('Statistics is disabled because pandas and/or sweetviz could not be imported')


        columns       = [self.name]
        variable_data = self.__series
        first_value   = variable_data[0]

        if type(first_value) is list:
            list_len = len(first_value)
            columns = [f'{self.name}_X', f'{self.name}_Y', f'{self.name}_Z']
            if list_len == 4:
                columns.append(f'{self.name}_Q') 
        
        df = pd.DataFrame(variable_data, columns=columns ) 

        try:
            from IPython.display import display
            display(df.describe(include='all').T)
        except:
            print(df.describe(include='all').T)
        

        try:
            import sweetviz as sv
        except ImportError:
            print( "Histogram plots require the sweetviz library to be imported. (pip import sweetviz)")
        else:
            sv.config_parser['Layout']['show_logo'] = '0' 
            sv_report = sv.analyze(df, pairwise_analysis="off" )

            if output_html:
                sv_report.show_html(filepath=f'{self.name}_Report.html')
            else:
                sv_report.show_notebook(w="90%", h="full", layout='vertical')


    def to_file(self, filename, verbose=True):
        '''Save series to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'name': self.__name, 'time': self.__mjd, 'series': self.__series}
            json.dump(contents, json_file)
            if verbose:
                print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename):
        '''Load series from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['name'], contents['time'], contents['series'])

    def summarize(self):
        hfill()
        print("Sedaro Simulation Series Summary".center(HFILL))
        print(f"'{self.name}'".center(HFILL))
        hfill()
        average_step = self.duration / len(self.elapsed_time)
        print(f"📈 {len(self)} points covering {self.duration/60:.1f} minutes with ~{average_step:.1f}s steps")

        if self.__has_subseries:
            print("\n📑 This series has subseries.")
            print(f"\n🗂️ Value data types are:")
            for key, value in self.__dtype.items():
                if value == 'None':
                    print(f"    - '{key}': All entries in this subseries are None")
                else:
                    print(f"    - '{key}': '{value}'")

        else:
            if self.__dtype == 'None':
                print('\n⛔ All entries in this series are None')
            else:
                print(f"\n🗂️ Value data type is '{self.__dtype}'")

        hfill()
        if self.__has_subseries:
            print("❓ Index [<SUBSERIES_NAME>] to select a subseries")
        else:
            print("❓ Call .plot to visualize results")
            print("📊 Display statistics with .stats( output_html=False ) ")
