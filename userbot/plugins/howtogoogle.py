#Modded from dagd.py
"""
Animate How To Google
Command .ggl Search Query
By @loxxi
"""

import os
import requests
import json


@client.on(events(pattern="ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("[{}]({})\n`Thank me Later 🙃` ".format(input_str,response_api.rstrip()))
    else:
        await event.edit("something is wrong. please try again later.")


HELPER.update({"howtogoogle": "\
**Available commands in howtogoogle module:**\
\n`.ggl <text>`\
"})
