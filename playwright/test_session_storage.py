import time

from playwright.sync_api import Playwright

from utils.APIUtils import APIUtils


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token into session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_role('button', name='ORDERS').click()
    #time.sleep(5)
    context.close()
    browser.close()