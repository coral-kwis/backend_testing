import random

from src.utilities.dbUtil import DBUtil
from src.utilities.loggerUtil import logger


class ProductsDao(DBUtil):
    # TABLE
    TBL_PRODUCTS = 'posts'

    # DATA TABLE COLUMNS
    DB_COL_PROD_ID = 'ID'
    DB_COL_PROD_TITLE = 'post_title'
    DB_COL_PROD_TYPE = 'post_type'
    DB_COL_PROD_POST_DATE = 'post_date'

    def __init__(self):
        logger().debug('-------------------------Products Dao-----------------------')
        super().__init__()

    def execute_select_random_products(self, qty=1):
        table = f'{self.database}.{self.table_prefix}{self.TBL_PRODUCTS}'
        sql = f'''SELECT * FROM {table} 
                    WHERE {self.DB_COL_PROD_TYPE}="product" 
                    ORDER BY {self.DB_COL_PROD_ID} DESC LIMIT 1000'''
        return random.sample(self.execute_select(sql), k=qty)

    def execute_select_products_created_after_given_date(self, given_date):
        table = f'{self.database}.{self.table_prefix}{self.TBL_PRODUCTS}'
        sql = f'''SELECT * FROM {table} 
                    WHERE {self.DB_COL_PROD_TYPE}="product"
                    AND {self.DB_COL_PROD_POST_DATE} > "{given_date}"'''
        return self.execute_select(sql)

    def execute_select_product_by_product_id(self, product_id):
        table = f'{self.database}.{self.table_prefix}{self.TBL_PRODUCTS}'
        sql = f'''SELECT * FROM {table} 
                            WHERE {self.DB_COL_PROD_ID}="{product_id}"'''
        return self.execute_select(sql)[0]

    def get_product_id_list_from_rs_db(self, db_prods_dict):
        return [prod[self.DB_COL_PROD_ID] for prod in db_prods_dict]
