import pytest
from pytest_bdd import given, when, then, scenarios

from pageObjects.login import LoginPage
from utils.APIUtilsFramework import APIUtils

user_credentials = {'email': 'subhbhatewera@yopmail.com', 'password': 'Rsa$4321'}
product_name = 'ZARA COAT 3'

scenarios('features/Orders.feature')

@pytest.fixture
def shared_data():
    return {}

@given('An Order is already placed using API')
def place_order(playwright, shared_data):
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = order_id

@given('The user is on the landing page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data['login'] = login_page

@when('User login to applicaiton')
def login(shared_data):
    login_page = shared_data['login']
    dashboard = login_page.login(user_credentials['email'], user_credentials['password'])
    shared_data['dashboard'] = dashboard

@when('Navigate to the Orders page')
def navigate_to_orders(shared_data):
    dashboard = shared_data['dashboard']
    order_history = dashboard.click_orders_link()
    shared_data['order_history'] = order_history

@when('Selects the order')
def select_order(shared_data):
    order_history = shared_data['order_history']
    order_details = order_history.select_order(shared_data['order_id'])
    shared_data['order_details'] = order_details

@then('Verify the Order details')
def verify_order_details(shared_data):
    order_details = shared_data['order_details']
    order_details.verify_order_details(product_name)