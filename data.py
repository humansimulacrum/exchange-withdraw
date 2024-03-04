# Get your API key from 0x here: https://dashboard.0x.org/apps
API_0x = 'your_0x_api_key'
# Get your API key from 1inch here: https://portal.1inch.dev/login
API_1inch = 'your_0x_api_key'


# API keys for exchanges. You can skip this if you don't use exchanges.
CEX_KEYS = {
    'binance': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'mexc': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'kucoin': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password'},
    'huobi': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'bybit': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
    'bitget': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret', 'password': 'your_api_password'},
    'coinex': {'api_key': 'your_api_key', 'api_secret': 'your_api_secret'},
}

# You can add any number of OKX accounts in the following format. This allows you to avoid constantly entering data for new accounts and simply reference them by name.
OKX_KEYS = {
    'account_1': {
        'api_key': 'your_api_key',
        'api_secret': 'your_api_secret',
        'password': 'your_api_password',
    },
    'account_2': {
        'api_key': 'your_api_key',
        'api_secret': 'your_api_secret',
        'password': 'your_api_password',
    },
}
