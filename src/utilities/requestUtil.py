import json

import requests
from assertpy import assert_that
from requests_oauthlib import OAuth1

from src.commons import constants
from src.commons.enums import StatusCode
from src.configs.hosts_config import API_HOST
from src.utilities.credentialUtil import CredentialUtil
from src.utilities.loggerUtil import logger


class RequestUtil(object):
    def __init__(self):
        env = constants.ENV
        self.base_url = API_HOST[env]['host']
        creds = CredentialUtil.get_wc_api_keys()
        self.auth = OAuth1(creds['wc_key'], creds['wc_secret'])

    def get(self, endpoint, payload=None, headers=None, expected_status_code=StatusCode.OK.value):
        logger().debug(f'API GET - payload: {payload}')
        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_api = rs_api.json()  # rs_api.json() return 'content' of response
        self.assert_status_code()
        return self.rs_api

    def post(self, endpoint, payload=None, headers=None, expected_status_code=StatusCode.CREATED.value):
        logger().debug(f'API POST - payload: {payload}')
        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_api = rs_api.json()
        self.assert_status_code()
        return self.rs_api

    def put(self, endpoint, payload=None, headers=None, expected_status_code=StatusCode.OK.value):
        logger().debug(f'API PUT - payload: {payload}')
        if not headers:
            headers = {'Content-Type': 'application/json'}
        self.url = self.base_url + endpoint
        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_api = rs_api.json()
        self.assert_status_code()
        return self.rs_api

    def assert_status_code(self):
        logger().debug(f'Actual status code is {self.status_code}\nApi response: {self.rs_api}')
        assert_that(self.status_code,
                    f'Expected status code is {self.expected_status_code}'
                    f'\nBut actual status code is {self.status_code}'
                    f'\nURL: {self.url} \nApi response: {self.rs_api}'
                    ).is_equal_to(self.expected_status_code)

    def assert_status_error(self, response, expected_status_error):
        assert_that(response[self.API_KEY_STATUS_ERROR],
                    f'Error code is not correct. Expected: "{expected_status_error}". '
                    f'Acutual: "{response[self.API_KEY_STATUS_ERROR]}"'
                    ).is_equal_to(expected_status_error)

    def assert_status_message(self, response, expected_status_message):
        assert_that(response[self.API_KEY_STATUS_MSG],
                    f'Error message is not correct. Expected: "{expected_status_message}". '
                    f'Acutual: "{response[self.API_KEY_STATUS_MSG]}"'
                    ).is_equal_to(expected_status_message)

    @staticmethod
    def verify_response_is_not_empty(response):
        assert_that(response, 'API response is empty').is_true()

    # API KEY
    API_KEY_STATUS_ERROR = 'code'
    API_KEY_STATUS_MSG = 'message'
