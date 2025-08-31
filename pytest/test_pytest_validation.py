import pytest


@pytest.fixture(scope="function")
def setUp():
    print('Setting up the browser')

@pytest.fixture(scope='function')
def secondWork():
    print("This will execute fist")
    yield
    print("The statement will execute at last because it's part of yield")

@pytest.mark.skip
def test_first_test(setUp):
    print('This is a first test')

@pytest.mark.myTag
def test_second_test(globalSetup, secondWork):
    print('This is Second test')