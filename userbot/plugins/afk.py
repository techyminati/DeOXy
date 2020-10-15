"""AFK Plugin for @UniBorg
Syntax: .afk REASON"""
import asyncio
import datetime
from datetime import datetime
from telethon.tl import functions, types



global USER_AFK  
global afk_time  
global last_afk_message  
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}


@client.on(events(pattern="afk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if not USER_AFK:  
        last_seen_status = await client(  
            functions.account.GetPrivacyRequest(
                types.InputPrivacyKeyStatusTimestamp()
            )
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  
        USER_AFK = f"yes: {reason}"  
        if reason:
            await client.send_message(event.chat_id, f"**I shall be Goin' afk!** __cuz ~ {reason}__")
        else:
            await client.send_message(event.chat_id, f"**I am Goin' afk!**")
        await asyncio.sleep(5)
        await event.delete()
        try:
            await client.send_message(  
                Config.PRIVATE_GROUP_BOT_API_ID,  
                f"Set AFK mode to True, and Reason is {reason}"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  


@client.on(events())
async def set_not_afk(event):
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  
        shite = await client.send_message(event.chat_id, "__Back alive :P!__\n**No Longer **AFK** .**\n `Was afk for:``" + total_afk_time + "`")
        try:
            await client.send_message(  
                Config.PRIVATE_GROUP_BOT_API_ID,  
                "Set AFK mode to False"
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await client.send_message(  
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` " + \
                "for the proper functioning of afk functionality " + \
                "Failed `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFK = {}  
        afk_time = None  


@client.on(events(incoming=True, func=lambda e: bool(e.mentioned or e.is_private)))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  
    global afk_time  
    global last_afk_message  
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    afk_since = "**a while ago**"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:  
        if afk_time:  
            now = datetime.datetime.now()
            datime_since_afk = now - afk_time  
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Yesterday**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` **ago**"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` **ago**"
            else:
                afk_since = f"`{int(seconds)}s` **ago**"
        msg = None
        message_to_reply = f"__My Master Has Been Gone **AFK** For__ `{total_afk_time}`\nWhere He Is: ~~ONLY GOD KNOWS~~ " + \
            f"\n\n__I promise I'll back in a few light years__\n**REASON**: {reason}" \
            if reason \
            else f"**Hey Nibba!**\n__I am currently AFK oof. Since when, you ask? For {total_afk_time} I guess.__\n\nWhen will I be back? ~~Soon~~ cuz always ded__Whenever I feel like it__**( ಠ ʖ̯ ಠ)**  "
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  
            await last_afk_message[event.chat_id].delete()  
        last_afk_message[event.chat_id] = msg  

HELPER.update({
    "afk": "\
**Requested Module --> afk**\
\n\n**Detailed usage of fuction(s):**\
\n\n`.afk <optional_reason>`\
\nUsage: Changes afk mode to **true**.\
"
})        
