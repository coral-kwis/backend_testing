import pytest

from src.commons.enums import StatusCode, StatusErr, StatusMsg
from src.dao.customers_dao import CustomersDao
from src.helpers.customers_helper import CustomersHelper
from src.utilities import genericUtil
from tests.testBase import TestBase

pytestmark = [pytest.mark.smoke, pytest.mark.customers]


class TestCreateCustomersSmoke(TestBase):
    @pytest.mark.tcid29(description='Verify "POST /customers" creates user with email and password only')
    def test_create_customer_with_email_and_password_only(self):
        email = genericUtil.generate_random_email()
        password = genericUtil.generate_random_password()
        rs_api = CustomersHelper().call_post_create_a_customer(email, password)
        self.assert_string_equal(rs_api[CustomersHelper.API_KEY_EMAIL], email)
        self.assert_string_equal(rs_api[CustomersHelper.API_KEY_FIRST_NAME], '')
        rs_dao = CustomersDao().execute_select_customer_by_email(email)
        self.assert_string_equal(rs_dao[CustomersDao.DB_COL_ID], rs_api[CustomersHelper.API_KEY_ID])

    @pytest.mark.tcid47(description='Verify "create customer" fails if email exists')
    def test_create_customer_fail_for_existing_email(self):
        rs_db = CustomersDao().execute_select_random_customers()[0]
        email = rs_db[CustomersDao.DB_COL_EMAIL]
        cust_helper = CustomersHelper()
        rs_api = cust_helper.call_post_create_a_customer(email=email, expected_status_code=StatusCode.BAD_REQUEST.value)
        cust_helper.assert_status_error(rs_api, StatusErr.EMAIL_EXIST.value)
        cust_helper.assert_status_message(rs_api, StatusMsg.EMAIL_EXIST.value)
