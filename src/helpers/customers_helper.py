from src.commons.enums import StatusCode
from src.utilities import genericUtil
from src.utilities.loggerUtil import logger
from src.utilities.requestUtil import RequestUtil


class CustomersHelper(RequestUtil):
    # ENDPOINT
    EP_CUSTOMERS = 'customers'

    # API KEYS
    API_KEY_ID = 'id'
    API_KEY_EMAIL = 'email'
    API_KEY_PASSWORD = 'password'
    API_KEY_FIRST_NAME = 'first_name'
    API_KEY_PER_PAGE = 'per_page'
    API_KEY_PAGE = 'page'

    def __init__(self):
        logger().debug('-------------------------Customers Helper-----------------------')
        super().__init__()

    def call_get_list_all_customers(self, payload=None):
        all_custs = []
        if not payload:
            payload = dict()
        if self.API_KEY_PER_PAGE not in payload.keys():
            payload[self.API_KEY_PER_PAGE] = 20
        page = 1
        while True:
            payload[self.API_KEY_PAGE] = page
            rs_api = self.get(endpoint=self.EP_CUSTOMERS, payload=payload)
            if not rs_api:
                break
            else:
                all_custs.extend(rs_api)
                page += 1
        return all_custs

    def call_post_create_a_customer(self, email=None, password=None, expected_status_code=StatusCode.CREATED.value,
                                    **kwargs):
        if not email:
            email = genericUtil.generate_random_email()
        if not password:
            password = genericUtil.generate_random_password()
        payload = {self.API_KEY_EMAIL: email, self.API_KEY_PASSWORD: password}
        payload.update(kwargs)
        return self.post(self.EP_CUSTOMERS, payload=payload, expected_status_code=expected_status_code)
