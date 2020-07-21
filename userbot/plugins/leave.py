# For @UniBorg
# Courtesy @yasirsiddiqui

"""
#syntax .leave
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
from global_variables_sql import SYNTAX, MODULE_LIST
import time

MODULE_LIST.append("leave")

@borg.on(admin_cmd("leave", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`Chat Leave Request Proceeded`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Unable To Leave - Not A Chat`')


SYNTAX.update({
    "leave": f"\
**Requested Module --> Chat Leaver**\
\n\nDetailed usage of fuction(s):\
\n\n```.leave```\
\nUsage: Leaves The Current Chat/Group.\
"
})            
