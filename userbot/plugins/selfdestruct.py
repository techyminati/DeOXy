# For @UniBorg
# courtesy Yasir siddiqui
"""Self Destruct Plugin
.sd <time in seconds> <text>
"""


import time

from telethon.errors import rpcbaseerrors
import importlib.util



@client.on(events(pattern="sd"))
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    if not destroy.text[0].isalpha() and destroy.text[0] not in ("/", "#", "@", "!"):
        message = destroy.text
        counter = int(message[4:6])
        text = str(destroy.text[6:])
        text = (
            text
            + "\n\nDestruction Level:  "
            + str(counter)
            + " seconds"
        )
        await destroy.delete()
        smsg = await destroy.client.send_message(destroy.chat_id, text)
        time.sleep(counter)
        await smsg.delete()


HELPER.update({"selfdestruct": "\
**Available commands in selfdestruct module:**\
\n`.sd`\
"})
