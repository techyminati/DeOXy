""".admin Plugin for @UniBorg"""
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events(pattern="warn1"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`You Have  1/3  warnings...\nWatch out!....\nReason for warn: Spam Demand`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events(pattern="warn2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`You Have  2/3  warnings...\nWatch out!....\nReason for last warn: Spam Demand`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events(pattern="warn3"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`You Have  3/3  warnings...\nBanned!!!....\nReason for ban: Spam Demand`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events(pattern="warn0"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Warning Resetted By Admin...\nYou Have  0/3  warnings`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@client.on(events(pattern="ocb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Warning..\n\nBattery Below 10%, Please Charge Your Phone**"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@client.on(events(pattern="fw"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`U Got A FloodWait:\nReason:telethon.errors.rpcerrorlist.FloodWaitError: A wait of 546578265716823 seconds is required (caused by EditMessageRequest)`"
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


HELPER.update({"warnbun": "\
**Available commands in warnbun module:**\
\n`.warn1`\
\n`.warn2`\
\n`.warn3`\
\n`.warn0`\
\n`.ocb`\
\n`.fw`\
"})
