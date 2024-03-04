import asyncio
import random

from loguru import logger

from setting import IS_SLEEP, DELAY_SLEEP
from modules.utils.files import read_txt

from modules.exchange_withdraw import ExchangeWithdraw, OkxWithdraw


WALLETS = read_txt("datas/wallets.txt")


MODULES = {
    1: ("exchange_withdraw", ExchangeWithdraw),
    2: ("okx_withdraw", OkxWithdraw)
}


def get_module(module):
    module_info = MODULES.get(module)
    if module_info:
        module_name, func = module_info
        return func, module_name
    else:
        raise ValueError(f"Unsupported module: {module}")


async def process_exchanges(func, wallets):
    for address in wallets:
        exchange = func(address)
        res = await exchange.start()
        if IS_SLEEP and res:
            time_sleep = random.randint(*DELAY_SLEEP)
            logger.info(f'sleep for {time_sleep} sec.')
            await asyncio.sleep(time_sleep)


async def main(module):
    func = get_module(module)
    await process_exchanges(func, WALLETS)
