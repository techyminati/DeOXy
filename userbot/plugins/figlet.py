import pyfiglet
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("figlet")

SYNTAX.update({
    "figlet": "\
**Requested Module --> Figletter Module**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.figlet <text>```\
\nUsage: Figlets the text.\
"
})        

@command(pattern="^.figlet ?(.*)", outgoing=True)
async def figlet(event):
    if event.fwd_from:
        return
    CMD_FIG = {"slant": "slant", "3D": "3-d", "5line": "5lineoblique", "alpha": "alphabet", "banner": "banner3-D", "doh": "doh", "iso": "isometric1", "letter": "letters", "allig": "alligator", "dotm": "dotmatrix", "bubble": "bubble", "bulb": "bulbhead", "digi": "digital"}
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await event.edit("**DeOXy MASTER:** `No text detected`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await event.edit("**DeOXy MASTER:** `Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await event.respond("‌‌‎`{}`".format(result))
    await event.delete()
