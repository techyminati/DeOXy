# Credits --> @authoritydmc and Priyam Kalra
# A clean and beautiful alternative to .help
# Syntax (.modules)

@client.on(events(pattern="modules ?(.*)"))
async def modulelist(event):
    if event.fwd_from:
        return
    modcount = 1
    msg = "<strong>Available Modules:</strong>"
    title = ""
    for key in sorted(HELPER, key=lambda e: e.upper()):
        new_title = f"\n\n<strong>{key[0].upper()}</strong>\n"
        if new_title == title:
            title = "\n"
        else:
            title = new_title
        msg += f"{title}• <code>{key}</code>"
        title = new_title
        modcount += 1
    msg += f"\n\nNumber of modules: <strong>{modcount}</strong>\nSend <code>.help <module_name></code> to get help regarding a module."
    await event.edit(msg, parse_mode="HTML")
