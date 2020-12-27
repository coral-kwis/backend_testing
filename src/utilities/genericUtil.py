import random
import string
from datetime import datetime, timedelta

from src.utilities.loggerUtil import logger


def generate_random_email(domain=None, email_prefix=None):
    if not domain:
        domain = 'coral.com'
    if not email_prefix:
        email_prefix = 'test'
    email_length = random.randint(1, 20)
    random_email_string = ''.join(random.choices(string.ascii_letters + string.digits, k=email_length))
    email = email_prefix + '_' + random_email_string + '@' + domain
    logger().debug(f'email = {email}')
    return email


def generate_random_password():
    password_length = random.randint(8, 20)
    password = ''.join(random.choices(string.ascii_letters, k=password_length))
    logger().debug(f'password = {password}')
    return password


def generate_random_number(end, start=1):
    return random.randint(start, end)


def generate_random_string(string_length):
    return ''.join(random.choices(string.ascii_letters, k=string_length))


def convert_x_days_from_today_to_iso_format(x_days):
    date = datetime.now().replace(microsecond=0) - timedelta(days=x_days)
    return date.isoformat()


if __name__ == '__main__':
    x = convert_x_days_from_today_to_iso_format(30)
    date = datetime.now()
    breakpoint()
    print(x)
