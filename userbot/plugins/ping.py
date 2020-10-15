from datetime import datetime


@client.on(events(pattern="ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n{}".format(ms))


HELPER.update({"ping": "\
**Available commands in ping module:**\
\n`.ping`\
"})
