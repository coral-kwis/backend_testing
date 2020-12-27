import pytest

from src.commons.enums import OrderStatus, StatusErr, StatusMsg, StatusCode
from src.helpers.orders_helper import OrdersHelper
from src.utilities import genericUtil
from tests.testBase import TestBase

pytestmark = [pytest.mark.orders]


class TestUpdateOrders(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.order_helper = OrdersHelper()

    @pytest.mark.parametrize('new_status', [
        pytest.param(OrderStatus.CANCELLED.value,
                     marks=[pytest.mark.tcid55(description='Update order status to canceled')]),
        pytest.param(OrderStatus.COMPLETED.value,
                     marks=[pytest.mark.tcid56(description='Update order status to completed')]),
        pytest.param(OrderStatus.ON_HOLD.value,
                     marks=[pytest.mark.tcid56(description='Update order status to on-hold')])
    ])
    def test_update_order_status(self, new_status):
        order_rs_api = self.order_helper.call_post_create_an_order()
        payload = {OrdersHelper.API_KEY_ORDER_STATUS: new_status}
        update_rs_api = self.order_helper.call_put_update_an_order(order_id=order_rs_api[OrdersHelper.API_KEY_ORDER_ID],
                                                                   payload=payload)
        self.assert_string_equal(update_rs_api[OrdersHelper.API_KEY_ORDER_STATUS], new_status)

    @pytest.mark.tcid58(description='Update order status to random string')
    def test_update_order_status_to_random_string(self):
        order_rs_api = self.order_helper.call_post_create_an_order()
        new_status = 'abc123'
        payload = {OrdersHelper.API_KEY_ORDER_STATUS: new_status}
        update_rs_api = self.order_helper.call_put_update_an_order(order_id=order_rs_api[OrdersHelper.API_KEY_ORDER_ID],
                                                                   payload=payload,
                                                                   expected_status_code=StatusCode.BAD_REQUEST.value)
        self.order_helper.assert_status_error(update_rs_api, StatusErr.INVALID_PARAM.value)
        self.order_helper.assert_status_message(update_rs_api, StatusMsg.INVALID_STATUS.value)

    @pytest.mark.tcid59(description='Update order "customer_note"')
    def test_update_order_customer_note(self):
        order_rs_api = self.order_helper.call_post_create_an_order()
        order_id = order_rs_api[OrdersHelper.API_KEY_ORDER_ID]
        customer_note = genericUtil.generate_random_string(50)
        payload = {OrdersHelper.API_KEY_CUSTOMER_NOTE: customer_note}
        self.order_helper.call_put_update_an_order(order_id, payload)
        order_rs = self.order_helper.call_get_an_order(order_id)
        self.assert_string_equal(order_rs[OrdersHelper.API_KEY_CUSTOMER_NOTE], customer_note)
