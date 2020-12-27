import pytest

from src.commons import constants
from src.dao.products_dao import ProductsDao
from src.helpers.customers_helper import CustomersHelper
from src.helpers.orders_helper import OrdersHelper
from tests.testBase import TestBase

pytestmark = [pytest.mark.smoke, pytest.mark.orders]


class TestCreateOrdersSmoke(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self):
        prod_dao = ProductsDao()
        db_prods_dict = prod_dao.execute_select_random_products(qty=2)
        self.prod_id_list = prod_dao.get_product_id_list_from_rs_db(db_prods_dict)
        self.orders_helper = OrdersHelper()
        self.payload = self.orders_helper.create_order_payload_line_items(self.prod_id_list)

    @pytest.mark.tcid48(description='Create a paid order with guest customer')
    def test_create_a_paid_order_with_guest_customers(self):
        rs_api = self.orders_helper.call_post_create_an_order(self.payload)
        rs_prod_ids_list = self.orders_helper.get_product_id_list(rs_api)
        self.orders_helper.verify_response_is_not_empty(rs_api)
        self.assert_string_equal(rs_api[OrdersHelper.API_KEY_ORDER_CUST_ID], constants.GUEST_CUSTOMER_ID)
        self.assert_list_equal(rs_prod_ids_list, self.prod_id_list)

    @pytest.mark.tcid49(description='Create a paid order with new created customer')
    def test_create_a_paid_order_with_new_customer(self):
        new_cust_rs_api = CustomersHelper().call_post_create_a_customer()
        new_cust_id = new_cust_rs_api[CustomersHelper.API_KEY_ID]
        self.payload.update({OrdersHelper.API_KEY_ORDER_CUST_ID: new_cust_id})
        order_rs_api = self.orders_helper.call_post_create_an_order(self.payload)
        prod_ids_rs_api = self.orders_helper.get_product_id_list(order_rs_api)
        self.orders_helper.verify_response_is_not_empty(order_rs_api)
        self.assert_string_equal(order_rs_api[OrdersHelper.API_KEY_ORDER_CUST_ID], new_cust_id)
        self.assert_list_equal(prod_ids_rs_api, self.prod_id_list)
