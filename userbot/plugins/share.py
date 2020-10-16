import subprocess
import asyncio
import time


@client.on(events(pattern="plugins"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins:**\n`{o}`\n\n**TIP:** Use .send <plugin_name> to send the plugin and .install replied to the module to add the plugin to the userbot"
    await event.edit(OUTPUT)


HELPER.update({
    "share": "\
**Requested Module --> Sharing Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n`.plugins`\
\nUsage: Shows all the plugins.\
"
})    
