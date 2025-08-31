import json
import pytest
from playwright.sync_api import Playwright
from pageObjects.login import LoginPage
from utils.APIUtilsFramework import APIUtils

#Read the data from the json file
with open('data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_crdentials_list = test_data['user_credentials']

@pytest.mark.parametrize('user_credentials', user_crdentials_list)
@pytest.mark.smoke
def test_e2e_web_api(playwright:Playwright, browser_instance, user_credentials):
    product_name = 'ZARA COAT 3'


    #Create Order using APIUtils
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)

    login = LoginPage(browser_instance)
    login.navigate()
    dashboard = login.login(user_credentials['email'], user_credentials['password'])
    order_history = dashboard.click_orders_link()
    order_details = order_history.select_order(order_id)
    order_details.verify_order_details(product_name)



