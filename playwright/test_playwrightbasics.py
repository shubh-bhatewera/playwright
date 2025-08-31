import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto('https://bpd-hme-uat.seguesolutions.org/')
    browser.close()

#If you want to run tests in headless mode and only on chromium then you can use page fixture
def test_playwright_shortcut(page:Page):
    page.goto('https://bpd-hme-uat.seguesolutions.org/')

def test_core_locators(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('consult')
    page.get_by_role('button', name='Sign In').click()
    time.sleep(5)

def test_segue(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://bpd-segue-uat.seguesolutions.org/")
    page.get_by_placeholder('Username').fill('subhash.bhatewara')
    page.get_by_placeholder('Password').fill('Subhash@123')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_text('Invalid Username/Password')).to_be_visible()
    #time.sleep(5)

def test_firefox_browser(playwright: Playwright):
    firefox = playwright.firefox.launch(headless=False)
    context = firefox.new_context(viewport=None)
    page = context.new_page()
    page.goto("https://bpd-hme-uat.seguesolutions.org/")
    page.get_by_placeholder('Username').fill('subhash.bhatewara')
    page.get_by_placeholder('Password').fill('Subhash@123')
    page.get_by_role('button', name='Login').click()
    time.sleep(5)





