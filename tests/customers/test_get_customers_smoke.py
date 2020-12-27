import pytest

from src.dao.customers_dao import CustomersDao
from src.helpers.customers_helper import CustomersHelper
from tests.testBase import TestBase

pytestmark = [pytest.mark.customers, pytest.mark.smoke]


class TestGetCustomersSmoke(TestBase):
    @pytest.mark.tcid30(description='Verify "GET /customers" lists all users')
    def test_get_all_customers(self):
        cust_helper = CustomersHelper()
        rs_api = cust_helper.call_get_list_all_customers()
        cust_helper.verify_response_is_not_empty(rs_api)
        cust_db = CustomersDao().execute_select_all_customers()
        self.assert_string_equal(len(rs_api), len(cust_db))
