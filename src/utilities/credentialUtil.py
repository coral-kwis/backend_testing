from src.commons import constants


class CredentialUtil(object):
    @staticmethod
    def get_wc_api_keys():
        wc_key = constants.WC_KEY
        wc_secret = constants.WC_SECRET
        if not wc_key or not wc_secret:
            raise Exception('The API credentials "WC_KEY" & "WC_SECRET" must be in environment variables')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = constants.DB_USER
        db_password = constants.DB_PASSWORD
        if not db_user or not db_password:
            raise Exception('The DB credentials "DB_USER" and "DB_PASSWORD" must be in env variables')
        else:
            return {'db_user': db_user, 'db_password': db_password}
