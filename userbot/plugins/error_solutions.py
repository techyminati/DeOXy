# Exclusive module for PhoeniX
#Ported To DeOXy
# By @Techy05
# You should use this module without proper credits
# Syntax (.solution <error_name>)
from telethon import events
from userbot.utils import admin_cmd
import asyncio
from telethon.tl import functions, types
from global_variables_sql import SYNTAX, MODULE_LIST, ERROR, ERROR_LIST


MODULE_LIST.append("solution")

@borg.on(admin_cmd(pattern="solution ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        err = event.pattern_match.group(1)
        if err:
            if err in ERROR:
                await event.edit(ERROR[err])
            else:
                await event.edit("No information for this error yet!\n**Tip: Get a list of all errors using .errors**")
        else:
            await event.edit("Please specify an error.\n**Tip: Get a list of all errors using .errors**")
