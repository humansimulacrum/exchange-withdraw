from tracks import *

# --- Settings ---
WALLETS_IN_BATCH = 1    # How many wallets to run in one thread (simultaneously)

IS_SLEEP = True         # Enable/disable delay between wallets
DELAY_SLEEP = [30, 60]  # Delay range between wallets (seconds)
RANDOMIZER = True       # Enable/disable random wallet shuffling
RETRY = 0               # Number of retries on errors/failures

USE_PROXY = False       # Enable/disable proxy usage in web3 requests
CHECK_GWEI = True       # Enable/disable base Gwei checking
MAX_GWEI = 50           # Maximum Gwei (see https://etherscan.io/gastracker)


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

    exchange    = 'bitget' # Specify the exchange here

    chain       = 'BEP20' # In which network to withdraw
    symbol      = 'USDT' # Which token to withdraw

    amount_from = 1.5 # Withdrawal from a certain amount of coins
    amount_to   = 2.2 # Withdrawal up to a certain amount of coins

    is_private_key = False # Set to True if you have inserted EVM private keys in wallets.txt. Set to False if you have addresses (EVM / non-EVM).

    account = "spot" # spot | funding

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
    '''

    chain   = 'CORE'
    symbol  = 'CORE'

    amount_from = 0.7
    amount_to   = 1

    account = 'account_1'

    fee     = 0.001 # Withdrawal fee
    sub_acc = False # True / False. True if you want to check sub-accounts and first transfer from them to the main account

    is_private_key = False # Set to True if you have inserted EVM private keys in wallets.txt. Set to False if you have addresses (EVM / non-EVM).
