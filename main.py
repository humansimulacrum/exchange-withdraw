import asyncio

from runner import main

if __name__ == "__main__":

    MODULE = int(input('''
MODULE:
1.  exchange_withdraw
2.  okx_withdraw

Choose a module (1 - 2) : '''))

    asyncio.run(main(MODULE))
