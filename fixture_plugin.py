import pytest

@pytest.fixture(scope="function")
def eight_tc(request):
    input_param = request.config.getoption('--ip')
    log = request.config.getoption('--logs')
    if log:
        print("\n LOGS are saved")
    return input_param
