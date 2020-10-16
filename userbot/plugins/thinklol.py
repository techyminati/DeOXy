# (c) @UniBorg

import asyncio
from collections import deque


@client.on(events(pattern="lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤔🧐🤔🧐"))
	for _ in range(999):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    


HELPER.update({"thinklol": "\
**Available commands in thinklol module:**\
\n`.lol`\
"})
