# This Source Code Form is subject to the terms of the GNU

# General Public License, v.3.0. If a copy of the GPL was not distributed with this

# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html

# By @TechyNewbie



from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd





@borg.on(admin_cmd("restart"))
async def restart(event):

    if event.fwd_from:

        return

    await borg.send_message(

        event.chat_id,

        "**DeOXy MASTER:** `My Boss wishes you to stop using this bot for a minute`, **Approved**"

    )

    await event.delete()
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()



    

@borg.on(events.NewMessage(pattern=r"^.stop", from_users=767014786, incoming=True))

async def hitler(e):

    await restart(e)


