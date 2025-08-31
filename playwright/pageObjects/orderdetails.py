from playwright.sync_api import expect

class OrderDetails:

    def __init__(self, page):
        self.page = page

    def verify_order_details(self, product_name):
        expect(self.page.locator('.title')).to_have_text(product_name)