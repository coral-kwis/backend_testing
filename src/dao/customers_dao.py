import random

from src.utilities.dbUtil import DBUtil
from src.utilities.loggerUtil import logger


class CustomersDao(DBUtil):
    def __init__(self):
        logger().debug('-------------------------Customers Dao-----------------------')
        super().__init__()

    def execute_select_customer_by_email(self, email):
        table = f'{self.database}.{self.table_prefix}{self.TBL_USERS}'
        sql = f'SELECT * FROM {table} WHERE {self.DB_COL_EMAIL}="{email}";'
        return self.execute_select(sql)[0]

    def execute_select_random_customers(self, qty=1):
        table = f'{self.database}.{self.table_prefix}{self.TBL_USERS}'
        sql = f'SELECT * FROM {table} ORDER BY {self.DB_COL_ID} DESC LIMIT 1000;'
        return random.sample(self.execute_select(sql), k=qty)

    def execute_select_all_customers(self):
        table = f'{self.database}.{self.table_prefix}{self.TBL_USERS}'
        sql = f'SELECT * FROM {table} WHERE {self.DB_COL_USER_LOGIN} != "admin"'
        return self.execute_select(sql)

    # TABLE
    TBL_USERS = 'users'

    # DATA TABLE COLUMNS
    DB_COL_EMAIL = 'user_email'
    DB_COL_ID = 'ID'
    DB_COL_USER_LOGIN = 'user_login'
