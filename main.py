# before run this script install required packages via command below
# pip3 install -U pytgcalls==3.0.0.dev12

import asyncio

import pytgcalls
import pyrogram

from tgls_bot import APP_ID, API_HASH, CHAT_ID, BOT_TOKEN, OWNER_ID, INPUT_SOURCE

# EDIT THIS
# more info about API keys here https://docs.pyrogram.org/intro/setup#api-keys
API_ID = APP_ID   # '3607361'
API_HASH = API_HASH     # 'c57bcc4b09591db4f90f60b469e8870f'
BOT_TOKEN = BOT_TOKEN   # "1725624123:AAEk5bSDRZoWpECQf3CAgrjBPEB6esHmXx8"

CHAT_ID = CHAT_ID   # '@ufstest'    # it can be a channel too
INPUT_SOURCE = INPUT_SOURCE     # 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
# EDIT END


async def main(client):
    group_call = pytgcalls.GroupCallFactory(client).get_group_call()
    await group_call.join(CHAT_ID)
    await group_call.start_video(INPUT_SOURCE)

    await pyrogram.idle()


# if __name__ == '__main__':
#     pyro_client = pyrogram.Client(
#         'pytgcalls',
#         api_id=API_ID,
#         api_hash=API_HASH,
#         bot_token=BOT_TOKEN,
#     )
#     pyro_client.start()
#
#     asyncio.get_event_loop().run_until_complete(main(pyro_client))
