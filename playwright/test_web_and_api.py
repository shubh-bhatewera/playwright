import time
from playwright.sync_api import Playwright, expect
from utils.APIUtils import APIUtils

def test_web_and_api_e2e(playwright:Playwright):
    product_name = 'ZARA COAT 3'
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Crate Order via API
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)

    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_placeholder('email@example.com').fill('subhbhatewera@yopmail.com')
    page.get_by_placeholder('enter your passsword').fill('Rsa$4321')
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='ORDERS').click()
    order_row = page.locator('tr').filter(has_text=order_id)
    order_row.get_by_role('button', name='View').click()
    expect (page.locator('.title')).to_have_text(product_name)
    time.sleep(5)
    context.close()
    browser.close()
