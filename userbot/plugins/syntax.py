# Pirated from Priyam's The TG Bot 2.0
# A clean and beautiful alternative to .help
# Syntax (.syntax <module_name>)
import asyncio
from telethon.tl import functions, types



@client.on(events(pattern="syntax ?(.*)"))
async def _(event):
        if event.fwd_from:
            return
        module = event.pattern_match.group(1)
        if module:
            if module in HELPER:
                await event.edit(HELPER[module])
            else:
                await event.edit("Please specify a valid module.")
        else:
            await event.edit("Please specify a module.\n**Tip: Get a list of all modules using .modules**")
