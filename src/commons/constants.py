import os
# Reads the key-value pair from .env file and adds them to environment variable.
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# ENVIRONMENT VARIABLES
ENV = os.getenv('ENV', 'test')
MACHINE = os.getenv('MACHINE')
WC_KEY = os.getenv('WC_KEY')
WC_SECRET = os.getenv('WC_SECRET')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# CONTANTS VARIABLES
GUEST_CUSTOMER_ID = 0

# PATH
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
