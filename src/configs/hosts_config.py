API_HOST = {
    'test': {
        'host': 'http://127.0.0.1/wp-json/wc/v3/'
    },
    'dev': {
        'host': ''
    },
    'prod': {
        'host': ''
    }
}

DB_HOST = {
    'WIN': {
        'test': {
            'host': '127.0.0.1',
            'database': 'wp236',
            'table_prefix': 'wpwz_',
            'port': '3306'
        }
    },
    'MAC': {
        'test': {
            'host': 'localhost',
            'database': 'wp236',
            'table_prefix': '',
            'socket': None,
            'port': '3306'
        }
    }
}
