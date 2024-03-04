# --- Settings ---
IS_SLEEP = True         # Enable/disable delay between wallets
DELAY_SLEEP = [120, 240]  # Delay range between wallets (seconds)
RETRY = 0               # Number of retries on errors/failures


class Value_Exchange:

    '''
    Withdraw coins from an exchange.
    Exchanges: binance | bybit | kucoin | mexc | huobi | bitget | coinex | bingx

    Chains:
    - binance: ETH | BEP20 | AVAXC | MATIC | ARBITRUM | OPTIMISM | APT
    - bybit
    - kucoin
    - mexc
    - huobi
    - bitget: zkSyncEra | ArbitrumNova | ArbitrumOne | ETH / ERC20 | Optimism | BEP20 | TRC20 | Polygon | Aptos | CELO | CoreDAO | Harmony
    - coinex
    - bingx
    - ascendex
    '''

    exchange = 'bitget'  # Specify the exchange here

    chain = 'BEP20'  # In which network to withdraw
    symbol = 'USDT'  # Which token to withdraw

    amount_from = 1.5  # Withdrawal from a certain amount of coins
    amount_to = 2.2  # Withdrawal up to a certain amount of coins

    account = "spot"  # spot | funding


class Value_OKX:

    '''
    OKX
    BSC
    ERC20
    TRC20
    Polygon
    Avalanche C-Chain
    Avalanche X-Chain
    Arbitrum One
    Optimism
    Fantom
    zkSync Era
    StarkNet
    Linea
    '''

    chain = 'Linea'
    symbol = 'ETH'

    amount_from = 0.004
    amount_to = 0.007

    account = 'withdraw'

    fee = 0.0002  # Withdrawal fee
    sub_acc = False  # True / False. True if you want to check sub-accounts and first transfer from them to the main account
