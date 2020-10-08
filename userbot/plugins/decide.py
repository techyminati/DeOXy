"""Quickly make a decision
Syntax: .decide"""
from telethon import events
import requests
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("decide")

SYNTAX.update({
    "decide": "\
**Requested Module --> Decider Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.decide```\
\nUsage: Hepls you in an situation where you are unable to say yes or no.\
"
})        

@borg.on(admin_cmd("decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await borg.send_message(
        event.chat_id,
        r["answer"],
        reply_to=message_id,
        file=r["image"]
    )
    await event.delete()
