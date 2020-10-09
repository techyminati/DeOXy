#Imported to DeOXy

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot import bot, BOTLOG_CHATID, ALIVE_NAME, CMD_LIST
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
client = telebot = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
ALIVE_NAME = str(ALIVE_NAME) 
from telethon.events import ChatAction
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("global_rights")

SYNTAX.update({
    "global_rights": "\
**Requested Module --> Global Rights Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.gban```\
\nUsage: Globally bans a user everywhere you admin in.\
\n\n```.ungban```\
\nUsage: UnGlobally bans a user everywhere you admin in.\
\n\n```.gmute```\
\nUsage: Globally mutes a user everywhere you admin in.\
\n\n```.ungmute```\
\nUsage: Globally unmutes a user everywhere you admin in.\
"
})        

# Imported from @javes05
# Kangers keep the credits -_-

@command(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def startgban(tb): 
   oof = tb ; sender = await oof.get_sender() ; me = await oof.client.get_me()
   if not sender.id == me.id:
        tele = await oof.reply("`Processing...`")
   else:
    	tele = await oof.edit("`Processing...`")      
   me = await tb.client.get_me() ; await tele.edit(f"`{ALIVE_NAME}:` **Globally Banning user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await tb.get_chat() ; a = b = 0
   if tb.is_private:       
   	user = tb.chat ; reason = tb.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = tb.chat.title  
   try:       
    user, reason = await get_user_from_event(tb)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await tele.edit(f"`{ALIVE_NAME}:`**User not found.**")
   if user:      
        if user.id == 767014786:     
    	             return await tele.edit(f"`{ALIVE_NAME}:`**DeOXy MASTER: Denied.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute            
        except:
   	     pass
        try:
          await tb.client(BlockRequest(user))
          block = 'True'
        except:      
           pass
        testtb = [d.entity.id for d in await tb.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testtb:
            try:
                 await tb.client.edit_permissions(i, user, view_messages=False)          
                 a += 1
                 await tele.edit(f"`{ALIVE_NAME}:` **Global Banning User!\nGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await tele.edit(f"`{ALIVE_NAME}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await tele.edit(f"`{ALIVE_NAME}:`**DeOXy MATER: User already Gbanned**")
   except:
    	pass
   return await tele.edit(f"`{ALIVE_NAME}:` **Gbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) **") 
 
@command(outgoing=True, pattern="^;ungban(?: |$)(.*)")
async def regressgban(tb):
   oof = tb ; sender = await oof.get_sender() ; me = await oof.client.get_me()
   if not sender.id == me.id:
        tele = await oof.reply("`Processing...`")
   else:
    	tele = await oof.edit("`processing...`")   
   me = await tb.client.get_me() ; await tele.edit(f"`{ALIVE_NAME}:` **Requesting  to UnGban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await tb.get_chat() ; a = b = 0
   if tb.is_private:       
   	user = tb.chat ; reason = tb.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = tb.chat.title  
   try:       
    user, reason = await get_user_from_event(tb)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await tele.edit(f"`{ALIVE_NAME}:`**DeOXy MASTER: User not found. Invalid argument**")
   if user:      
        if user.id == 767014786:     
    	             return await tele.edit(f"`{ALIVE_NAME}:`**DeOXy MASTER: Denied.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
   	     pass
        try:
          await tb.client(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testtb = [d.entity.id for d in await tb.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testtb:
            try:
                 await tb.client.edit_permissions(i, user, send_messages=True)          
                 a += 1
                 await tele.edit(f"`{ALIVE_NAME}:` **Requesting  to ungban user!\nunGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await tele.edit(f"`{ALIVE_NAME}:` **DeOXy MASTER: User not found, Reply to a user**")        
   try:
     if ungmute(user.id) is False:
            return await tele.edit(f"`{ALIVE_NAME}:`**DeOXy MASTER: Invalid argument, Already Gbanned**")
   except:
    	pass
   return await tele.edit(f"`{ALIVE_NAME}:` **UnGbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) **") 
        
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully gmuted that person")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully ungmuted that person")

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully gmuted that person")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully ungmuted that person")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()   
