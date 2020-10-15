# For @UniBorg
"""Countdown Commands
.wchar"""

import asyncio

@client.on(events(pattern="wchar"))
async def timer_blankx(e):
    txt = '`Realmeme Wireless Charging (beta) Started...\nDevice Detected: Realmeme 1 (CPH1861)\nBattery Percentage:` '
    j = 10
    k = j
    for j in range(j):
        await e.edit(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await e.edit("`Realmeme Wireless Charging (beta) Completed...\nDevice Detected: Realmeme 1(Diamond Black Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ", link_preview=True)


HELPER.update({"wirelesscharge": "\
**Available commands in wirelesscharge module:**\
\n`.wchar`\
"})

