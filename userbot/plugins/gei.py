#By X-tra-Telegram Modz Geng
#Developed By @TechyNewbie
#Module made for mocking Priyam.
#Sorry Priyam, Don't take it seriously XD
#Syntax .gei"""

from telethon import events
import asyncio
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("gei")

SYNTAX.update({
    "gei": "\
**Requested Module --> Make it gei Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.gei```\
\nUsage: Lets make it gei.\
"
})        


@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 4)
    input_str = event.pattern_match.group(1)
    if input_str == "gei":
        await event.edit(input_str)
        animation_chars = [
            "**“It**",
            "**“It Is**",
            "**“It Is Gei”**",
            "**“It Is Gei”** __- Me__"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
