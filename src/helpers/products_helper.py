import json
import os

from assertpy import assert_that

from src.commons import constants
from src.commons.enums import StatusCode
from src.utilities.loggerUtil import logger
from src.utilities.requestUtil import RequestUtil


class ProductsHelper(RequestUtil):
    # ENDPOINT
    EP_PRODUCTS = 'products'

    # API_KEYS
    API_KEY_AFTER = 'after'
    API_KEY_PROD_ID = 'id'
    API_KEY_PROD_NAME = 'name'
    API_KEY_PROD_TYPE = 'type'
    API_KEY_PROD_PRICE = 'regular_price'
    API_KEY_PAGE = 'page'
    API_KEY_PER_PAGE = 'per_page'

    def __init__(self):
        logger().debug('-------------------------Products Helper-----------------------')
        super().__init__()

    def call_get_a_product(self, prod_id, expected_status_code=StatusCode.OK.value):
        return self.get(f'{self.EP_PRODUCTS}/{prod_id}', expected_status_code=expected_status_code)

    def call_get_list_all_products(self, payload=None, expected_status_code=StatusCode.OK.value):
        all_prods = []
        if not payload:
            payload = dict()
        if self.API_KEY_PER_PAGE not in payload.keys():
            payload[self.API_KEY_PER_PAGE] = 20
        page = 1
        while True:
            payload[self.API_KEY_PAGE] = page
            rs_api = self.get(self.EP_PRODUCTS, payload=payload, expected_status_code=expected_status_code)
            if rs_api:
                all_prods.extend(rs_api)
                page += 1
            else:
                break
        return all_prods

    def call_post_create_a_product(self, additional_payload=None, expected_status_code=StatusCode.CREATED.value):
        payload_temp_path = os.path.join(constants.ROOT_DIR, 'data', 'create_product_payload.json')
        with open(payload_temp_path) as file:
            payload = json.load(file)
        if additional_payload:
            assert_that(isinstance(additional_payload, dict),
                        f'Parameter additional_payloads must be a dictionary but found {type(additional_payload)}'
                        ).is_true()
            payload.update(additional_payload)
        return self.post(self.EP_PRODUCTS, payload=payload, expected_status_code=expected_status_code)

    def get_product_id_list_from_rs_api(self, prods_rs_api):
        return [prod[self.API_KEY_PROD_ID] for prod in prods_rs_api]
