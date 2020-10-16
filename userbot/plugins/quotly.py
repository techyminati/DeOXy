"""QuotLy: Avaible commands: .qbot
"""
import datetime
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

@client.on(events(pattern="qbot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Reply to any user message.`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("`Reply to text message`")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Reply to actual users message.`")
       return
    await event.edit("`Making a Quote`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events(incoming=True, from_users=chat))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`Please unblock me (@QuotLyBot) u Nigga`")
              return
          if response.text.startswith("Hi!"):
              await event.edit("`Can you kindly disable your forward privacy settings for good plox?`")
          else: 
              await event.delete()
              await event.client.send_message(event.chat_id, response.message)


HELPER.update({"quotly": "\
**Available commands in quotly module:**\
\n`.qbot <text>`\
"})
