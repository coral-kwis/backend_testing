import pytest

from src.dao.products_dao import ProductsDao
from src.helpers.products_helper import ProductsHelper
from src.utilities import genericUtil
from tests.testBase import TestBase

pytestmark = [pytest.mark.smoke, pytest.mark.products]


class TestCreateProductsSmoke(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.prod_helper = ProductsHelper()
        self.prod_dao = ProductsDao()
        self.random_prod_name = genericUtil.generate_random_string(10)
        self.payload = {ProductsHelper.API_KEY_PROD_NAME: self.random_prod_name}

    @pytest.mark.tcid26(description='Verify POST /products creates a simple product')
    def test_create_a_simple_product(self):
        prod_rs_api = self.prod_helper.call_post_create_a_product(additional_payload=self.payload)
        self.prod_helper.verify_response_is_not_empty(prod_rs_api)
        prod_rs_db = self.prod_dao.execute_select_product_by_product_id(prod_rs_api[ProductsHelper.API_KEY_PROD_ID])
        self.assert_true(prod_rs_db)
        self.assert_string_equal(prod_rs_db[ProductsDao.DB_COL_PROD_TITLE],self.random_prod_name)
