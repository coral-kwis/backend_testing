import pytest

from src.dao.products_dao import ProductsDao
from src.helpers.products_helper import ProductsHelper
from tests.testBase import TestBase

pytestmark = [pytest.mark.smoke, pytest.mark.products]


class TestGetProductsSmoke(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.prod_helper = ProductsHelper()
        self.prod_dao = ProductsDao()

    @pytest.mark.tcid24(description='"GET /products" does not return empty')
    def test_get_all_products(self):
        rs_api = self.prod_helper.call_get_list_all_products()
        self.prod_helper.verify_response_is_not_empty(rs_api)

    @pytest.mark.tcid25(description='Verify "products/id" returns a product with the given id')
    def test_get_product_by_id(self):
        prod_rs_db = self.prod_dao.execute_select_random_products()[0]
        db_prod_id = prod_rs_db[ProductsDao.DB_COL_PROD_ID]
        db_prod_name = prod_rs_db[ProductsDao.DB_COL_PROD_TITLE]
        prod_rs_api = self.prod_helper.call_get_a_product(db_prod_id)
        api_prod_name = prod_rs_api[ProductsHelper.API_KEY_PROD_NAME]
        self.assert_string_equal(api_prod_name, db_prod_name)
