# For @UniBorg
# Courtesy @yasirsiddiqui

"""
#syntax .leave
"""
from telethon.tl.functions.channels import LeaveChannelRequest
import time


@client.on(events(pattern="leave"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`Chat Leave Request Proceeded`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await client(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Unable To Leave - Not A Chat`')


HELPER.update({
    "leave": f"\
**Requested Module --> Chat Leaver**\
\n\nDetailed usage of fuction(s):\
\n\n`.leave`\
\nUsage: Leaves The Current Chat/Group.\
"
})            
