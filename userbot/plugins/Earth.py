# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

import asyncio
from collections import deque


@client.on(events(pattern="earth"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
HELPER.update({
    "solarsystem": f"\
**Requested Module --> Solar System**\
\n\nDetailed usage of fuction(s):\
\n\n\
\nUsage: Creates Cool solar system based Emojis.\n\
\n\nList of included animaes:\
\n`.Earth`\n\
\n`.moon`\n\
\n`.solarsystem`\n\
\n`.isro`\n\
"
})
