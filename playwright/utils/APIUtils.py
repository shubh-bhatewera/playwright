from playwright.sync_api import Playwright

ordersPayload = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "68a86429b01c5d7abb27e634"
        }
    ]
}

loginPalyload = {"userEmail": "subhbhatewera@yopmail.com", "userPassword": "Rsa$4321"}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/auth/login',
                                            data=loginPalyload)
        assert response.ok
        response_body = response.json()
        return response_body['token']


    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/')
        response = api_request_context.post('/api/ecom/order/create-order',
                                 data=ordersPayload,
                                 headers={'Authorization' : token,
                                          'Content-type': 'application/json'})

        response_body = response.json()
        order_id = response_body['orders'][0] #orders is a list so we need to get the value using the index
        print(order_id)
        return order_id