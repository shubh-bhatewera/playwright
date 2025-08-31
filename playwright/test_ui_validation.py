import time

from playwright.sync_api import Page, expect


def test_ui_validation_script(page: Page):
    products = ['iphone X', 'Nokia Edge']
    #Add 3 Items -> iPhoneX and Nokia Edge
    #Verify 2 items are added in Cart
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('consult')
    page.get_by_role('button', name='Sign In').click()
    for product_name in products:
        print(f"Product name -> {product_name}")
        product = page.locator('app-card').filter(has_text=product_name)
        product.get_by_role('button', name='Add ').click()
    page.get_by_text('Checkout').click()
    #page.locator('a.nav-link.btn.btn-primary').click()
    expect(page.locator('.media-body')).to_have_count(2)

    time.sleep(5)


def test_handle_childwindow(page: Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    with page.expect_popup() as newPageInfo:
        page.locator('.blinkingText').click()
        newPage = newPageInfo.value
        text = newPage.locator('.red').text_content()
        words = text.split('at')
        email = words[1].strip().split(' ')
        assert email[0] == 'mentor@rahulshettyacademy.com'


