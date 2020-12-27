import pymysql

from src.commons import constants
from src.configs.hosts_config import DB_HOST
from src.utilities.credentialUtil import CredentialUtil
from src.utilities.loggerUtil import logger


class DBUtil(object):
    def __init__(self):
        self.db_creds = CredentialUtil.get_db_credentials()
        machine = constants.MACHINE
        env = constants.ENV
        self.host = DB_HOST[machine][env]['host']
        self.database = DB_HOST[machine][env]['database']
        self.table_prefix = DB_HOST[machine][env]['table_prefix']

    def create_connection(self):
        logger().debug(f'Host: {self.host}, DB: {self.database}, credentials: {self.db_creds}')
        try:
            return pymysql.connect(host=self.host, user=self.db_creds['db_user'], password=self.db_creds['db_password'])
        except Exception as e:
            raise Exception(f'Failed connecting DB. Error: {str(e)}')

    def execute_select(self, sql):
        cnn = self.create_connection()
        logger().debug(f'sql: {sql}')
        try:
            cur = cnn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            logger().debug(f'rs_dict: {rs_dict}')
        except Exception as e:
            raise Exception(f'Failed running sql: {sql} \nError: {str(e)}')
        finally:
            cnn.close()
        return rs_dict
