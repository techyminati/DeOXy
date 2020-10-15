"""Quickly make a decision
Syntax: .decide"""
import requests


@client.on(events(pattern="decide"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    await client.send_message(
        event.chat_id,
        r["answer"],
        reply_to=message_id,
        file=r["image"]
    )
    await event.delete()


HELPER.update({"decide": "\
**Available commands in decide module:**\
\n`.decide`\
"})
