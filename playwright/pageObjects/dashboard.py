from .orderhistory import OrderHistory


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def click_orders_link(self):
        self.page.get_by_role('button', name='ORDERS').click()
        return OrderHistory(self.page)