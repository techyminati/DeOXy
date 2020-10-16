import sys
from telethon import functions, __version__


@client.on(events(pattern="mf ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in client._plugins:
        s_help_string = client._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    help_string = """
......................................../´¯/) 
......................................,/¯../ 
...................................../..../ 
..................................../´.¯/
..................................../´¯/
..................................,/¯../ 
................................../..../ 
................................./´¯./
................................/´¯./
..............................,/¯../ 
............................./..../ 
............................/´¯/
........................../´¯./
........................,/¯../ 
......................./..../ 
....................../´¯/
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
    """.format(
        sys.version,
        __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  
    if tgbotusername is not None:
        results = await client.inline_query(  
            tgbotusername,
            help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string + "\n\n" + s_help_string)
        await event.delete()


@client.on(events(pattern="dc"))
async def _(event):
    if event.fwd_from:
        return
    result = await client(functions.help.GetNearestDcRequest())  
    await event.edit(result.stringify())


@client.on(events(pattern="config"))
async def _(event):
    if event.fwd_from:
        return
    result = await client(functions.help.GetConfigRequest())  
    result = result.stringify()
    logger.info(result)  
    await event.edit("""Telethon UserBot powered by @UniBorg""")


HELPER.update({"mf": "\
**Available commands in mf module:**\
\n`.mf <text>`\
\n`.dc`\
\n`.config`\
"})
