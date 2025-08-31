import pytest


@pytest.fixture(scope='session')
def globalSetup():
    print('This is a global setup')