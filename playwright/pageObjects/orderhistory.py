from .orderdetails import OrderDetails


class OrderHistory:

    def __init__(self, page):
        self.page = page

    def select_order(self, order_id):
        order_row = self.page.locator('tr').filter(has_text=order_id)
        order_row.get_by_role('button', name='View').click()
        return OrderDetails(self.page)