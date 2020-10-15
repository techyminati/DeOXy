@client.on(events(pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for plugin in HELPER:
                string += "ℹ️ " + plugin + "\n"
                string += "\n"
            if len(string) > 4095:
                await client.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in HELPER:
                string = "Commands found in {}:\n".format(input_str)
                string += "    " + HELPER[input_str] + "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """Userbot Helper.. Provided by [𝔡𝓔𝐎𝕩𝕐](https://github.com/JAISHNAVPRASAD-DarklIous/DeOXy)\n
`Userbot Helper to reveal all the commands`\n__Do .help plugin_name for commands, in case popup doesn't appear.__"""
            results = await bot.inline_query(
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
