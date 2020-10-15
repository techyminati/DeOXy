#credits: @r4v4n4
import datetime
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

@client.on(events(pattern="frybot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("`Reply to any user message.`")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("`reply to text message`")
       return
    chat = "@image_deepfrybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Reply to actual users message.`")
       return
    await event.edit("`Processing`")
    async with client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events(incoming=True,from_users=chat))
              await client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("`Please unblock @sangmatainfo_bot and try again`")
              return
          if response.text.startswith("Forward"):
              await event.edit("`can you kindly disable your forward privacy settings for good?`")
          else: 
              await client.send_file(event.chat_id, response.message.media)


HELPER.update({"frybot": "\
**Available commands in frybot module:**\
\n`.frybot <text>`\
"})
