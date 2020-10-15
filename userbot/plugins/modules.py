# Credits --> @authoritydmc and Priyam Kalra
# A clean and beautiful alternative to .help
# Syntax (.modules)

@client.on(events(pattern="modules ?(.*)"))
async def modulelist(event):
    if event.fwd_from:
        return
    modcount = 1
    msg = "**Available Modules:**"
    title = ""
    for key in sorted(HELPER, key=lambda e: e.upper()):
        new_title = f"\n\n**{key[0].upper()}**\n"
        if new_title == title:
            title = "\n"
        else:
            title = new_title
        msg += f"{title}• {key}"
        title = new_title
        modcount += 1
    msg += f"\n\nNumber of modules: **{modcount}**\nSend .help <module_name> to get help regarding a module."
    await event.edit(msg)
    