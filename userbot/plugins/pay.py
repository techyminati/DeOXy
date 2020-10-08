""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("pay")

SYNTAX.update({
    "pay": "\
**Requested Module --> pay**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.pay```\
\nUsage: **pay**.\
"
})        



@borg.on(admin_cmd("pay"))
async def _(event):
    if event.fwd_from:
        return
    await client.send_file(
    file="pay.png",
    force_document=False,
    )
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
