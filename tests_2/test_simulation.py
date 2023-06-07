import time

from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID
from sedaro_2 import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def test_run_simulation():
    sim = sedaro.scenario_branch(WILDFIRE_SCENARIO_ID).simulation

    # Start simulation
    sim.start()
    print('- Started simulation')

    # Get status
    _check_job_status(sim.job())

    # Terminate
    print('- Terminating...')
    res = sim.terminate()
    print('-', res['message'])
    assert res['message'] == 'Successfully terminated simulation.'


def run_tests():
    test_run_simulation()
