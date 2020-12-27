import json
import os

from assertpy import assert_that

from src.commons import constants
from src.commons.enums import StatusCode
from src.utilities.loggerUtil import logger
from src.utilities.requestUtil import RequestUtil


class OrdersHelper(RequestUtil):
    # ENDPOINT
    EP_ORDERS = 'orders'

    # API KEY ORDERS
    API_KEY_ORDER_ID = 'id'
    API_KEY_ORDER_LINE_ITEMS = 'line_items'
    API_KEY_PROD_QUANTITY = 'quantity'
    API_KEY_ORDER_CUST_ID = 'customer_id'
    API_KEY_ORDER_PROD_ID = 'product_id'
    API_KEY_ORDER_STATUS = 'status'
    API_KEY_CUSTOMER_NOTE = 'customer_note'

    def __init__(self):
        logger().debug('-------------------------Orders Helper-----------------------')
        super().__init__()

    def call_get_an_order(self, order_id, expected_status_code=StatusCode.OK.value):
        return self.get(f'{self.EP_ORDERS}/{order_id}', expected_status_code=expected_status_code)

    def call_post_create_an_order(self, additional_payload=None, expected_status_code=StatusCode.CREATED.value):
        payload_temp_path = os.path.join(constants.ROOT_DIR, 'data', 'create_order_payload.json')
        with open(payload_temp_path) as file:
            payload = json.load(file)
        if additional_payload:
            assert_that(isinstance(additional_payload, dict),
                        f'Parameter additional_payloads must be a dictionary but found {type(additional_payload)}'
                        ).is_true()
            payload.update(additional_payload)
        return self.post(self.EP_ORDERS, payload=payload, expected_status_code=expected_status_code)

    def call_put_update_an_order(self, order_id, payload, expected_status_code=StatusCode.OK.value):
        return self.put(f'{self.EP_ORDERS}/{order_id}', payload=payload, expected_status_code=expected_status_code)

    def create_order_payload_line_items(self, prod_ids_list, qty=1):
        line_items = []
        for prod_id in prod_ids_list:
            line_items.append({self.API_KEY_ORDER_PROD_ID: prod_id, self.API_KEY_PROD_QUANTITY: qty})
        return {self.API_KEY_ORDER_LINE_ITEMS: line_items}

    def get_product_id_list(self, rs_api):
        return [item[self.API_KEY_ORDER_PROD_ID] for item in rs_api[self.API_KEY_ORDER_LINE_ITEMS]]
