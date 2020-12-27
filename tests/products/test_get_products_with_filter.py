import pytest

from src.dao.products_dao import ProductsDao
from src.helpers.products_helper import ProductsHelper
from src.utilities import genericUtil
from tests.testBase import TestBase

pytestmark = [pytest.mark.products]


class TestGetProductsWithFilter(TestBase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.prod_helper = ProductsHelper()
        self.prod_dao = ProductsDao()

    @pytest.mark.tcid51(description='Verify List Products with filter "after"')
    def test_list_products_with_filter_after(self):
        random_days = genericUtil.generate_random_number(100)
        after_date = genericUtil.convert_x_days_from_today_to_iso_format(random_days)
        payload = {ProductsHelper.API_KEY_AFTER: after_date}
        prods_rs_api = self.prod_helper.call_get_list_all_products(payload)
        prods_rs_db = self.prod_dao.execute_select_products_created_after_given_date(after_date)
        api_prod_id_list = self.prod_helper.get_product_id_list_from_rs_api(prods_rs_api)
        db_prod_id_list = self.prod_dao.get_product_id_list_from_rs_db(prods_rs_db)
        self.assert_list_equal(api_prod_id_list, db_prod_id_list)
