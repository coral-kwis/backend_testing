from src.utilities.dbUtil import DBUtil
from src.utilities.loggerUtil import logger


class OrdersDao(DBUtil):
    def __init__(self):
        logger().debug('-------------------------Orders Dao-----------------------')
        super().__init__()
