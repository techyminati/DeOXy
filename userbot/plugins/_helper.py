from userbot import CMD_LIST
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("userbot")

SYNTAX.update({
    "userbot": "\
**Requested Module --> Userbot main Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.load```\
\nUsage: Load a pre-existing module.\
\n\n```.unload```\
\nUsage: Unload a module.\
\n\n```.install```\
\nUsage: install a module.\
\n\n```.shutdown```\
\nUsage: Poweroff your userbot.\
\n\n```.restart```\
\nUsage: Restarts your userbot.\
\n\n```.plugins```\
\nUsage: See all the modules of the userbot.\
\n\n```.send <plugin_name>```\
\nUsage: Send a plugin.\
\n\n```.help```\
\nUsage: The legacy way of seeking help.\
"
})        

@command(pattern="^.help ?(.*)")
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Use `.modules` for a cleaner command view. Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """Userbot Legacy Look.. Provided by [𝔡𝓔𝐎𝕩𝕐](https://github.com/CyberJalagam/DeOXy)\n
`Use` `.plugins` `to reveal all the commands`\n"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
