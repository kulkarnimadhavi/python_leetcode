import pytest
import os
import yaml

pytest_plugins = ["pkg1.fixture_plugin"]

def pytest_addoption(parser):
    """
    Command line options for the pytest tests in this module.
    :param parser: Parser used for method.
    :return: None
    """
    parser.addoption("--ip",
                     action="store",
                     default='Eddie',
                     help="device configuration for comms testing")

    parser.addoption("--logs",
                     action="store_true",
                     help="Whether to save speaker logs for each test")

    parser.addoption("--data_file",
                     action="store",
                     default=None,
                     help="device configuration for comms testing")


#def pytest_configure(config):
 #   """
 #   Pytest built in method to import necessary plugins based on run time parameter.
 #   """
 #    config.pluginmanager.import_plugin("fixture_plugin)

def pytest_generate_tests(metafunc):
    """
    Look for device_control_test_data.yml file within the package that test is located. If it exists read the contents of the file
    and check to see if the test has a fixture matching an entry in the yaml file
    """
    data_file = metafunc.config.getoption('--data_file')
    test_data_file = os.path.dirname(metafunc.module.__file__) + "/{}.yml".format(data_file)
    if os.path.isfile(test_data_file):
        with open(test_data_file, 'r') as f:
            test_data = yaml.load(f, yaml.SafeLoader)
        for name, tests in test_data.items():
            if name in metafunc.fixturenames:
                fixture = name
                ids = [item['test_id'] for item in tests]
                metafunc.parametrize(fixture, tests, ids=ids)
        f.close()

@pytest.fixture(scope="session")
def hello(request):
    print("\n Hello Session")

    def teardown():
        print("\n Session ended")

    request.addfinalizer(teardown)

@pytest.fixture(scope="function")
def first_tc(request):
    print("\n Hello test case 1")

    def teardown():
        print("\n Test case 1 ended")
    request.addfinalizer(teardown)

@pytest.fixture(scope="function")
def second_tc():
    print("\n Hello test case 2")







@pytest.fixture(scope="function")
def third_tc(second_tc):
    print("\n Calling fixture from fixture")


@pytest.fixture(scope="function")
def fourth_tc():
    return 12345, 6789




@pytest.fixture(scope="function")
def fifth_tc():
    return {"fn":'Divya', "ln":"lastname"}


@pytest.fixture(scope="function")
def sixth_tc():
    def setup(device_type):
        print("\n print device type in fixture", device_type)
        return True
    return setup

@pytest.fixture(scope="function")
def seven_tc(request):
    input_param = request.config.getoption('--ip')
    log = request.config.getoption('--logs')
    if log:
        print("\n LOGS are saved")
    return input_param




#create a fixture
@pytest.fixture(scope="function")
def learn_conftest1():
    print("\n from conftest learning session 1")


#fixture calling another fixture
@pytest.fixture(scope="function")
def learn_conftest2(third_tc):
    print("\n from conftest learning test2  - fixture calling another fixture")


#fixture with teardown
@pytest.fixture(scope="function")
def learn_conftest3(request):
    month =6
    day = 13
    print("\n fixture that sets original month and date")

    def teardown():
        print("\n teardown function executes last with add finalizer")

    request.addfinalizer(teardown)
    return (month, day)

