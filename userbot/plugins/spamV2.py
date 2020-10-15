import asyncio
import time
from asyncio import wait

@client.on(events(pattern="tspam"))
async def tmeme(e):
     tspam = str(e.text[7:])
     message = tspam.replace(" ", "")
     for letter in message:
         await e.respond(letter)
     await e.delete()


HELPER.update({"spamV2": "\
**Available commands in spamV2 module:**\
\n`.tspam`\
"})
