# For UniBorg
# By Priyam Kalra
#Ported To X-tra MOD 2.0 By MrMobTech

from telethon.tl import functions, types
import time


@client.on(events(pattern="log ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    rep = await event.get_reply_message()
    msg = rep.text
    await log(msg)
    await event.delete()


async def log(text):
    LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
    await client.send_message(LOGGER, text)


HELPER.update({"logger": "\
**Available commands in logger module:**\
\n`.log <text>`\
"})
