from playwright.sync_api import Page

fake_response = {"data":[], "message":"No Orders"}

def intercept_resposne(route):
    route.fulfill(
        json=fake_response
    )


def test_network_1(page: Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', intercept_resposne)
    page.get_by_placeholder('email@example.com').fill('subhbhatewera@yopmail.com')
    page.get_by_placeholder('enter your passsword').fill('Rsa$4321')
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='ORDERS').click()
    message = page.locator('.mt-4').text_content()
    print(message)