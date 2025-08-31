import time

import pytest
from playwright.sync_api import Page

def intercept_request(route):
    route.continue_(url='https://rahulshettyacademy.com/client/#/dashboard/order-details/6711dcafae2afd4c0b9f6b66')

@pytest.mark.smoke
def test_network_2(page: Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*', intercept_request)
    page.get_by_placeholder('email@example.com').fill('subhbhatewera@yopmail.com')
    page.get_by_placeholder('enter your passsword').fill('Rsa$4321')
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='ORDERS').click()
    page.get_by_role('button', name='View').first.click()
    time.sleep(5)