"""Get ID of any Telegram media, or any user
Syntax: .get_id"""
from telethon import events
from telethon.utils import pack_bot_file_id
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("id")

SYNTAX.update({
    "id": "\
**Requested Module --> ID Fetcher Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.id```\
\nUsage: Fetches the user ID.\
"
})        


@borg.on(admin_cmd("id"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        chat = await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(str(event.chat_id), str(r_msg.from_id), bot_api_file_id))
        else:
            await event.edit("Current Chat ID: `{}`\nFrom User ID: `{}`".format(str(event.chat_id), str(r_msg.from_id)))
    else:
        await event.edit("Current Chat ID: `{}`".format(str(event.chat_id)))
