"""Available Commands:

.younoob
.menoob
.youpro
.mepro

@arnab431"""


import asyncio




@client.on(events(pattern="(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "younoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB" ,
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)
            
@client.on(events(pattern="(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "menoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB" ,
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval) 
            
@client.on(events(pattern="(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "youpro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu" ,
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)  
            
@client.on(events(pattern="(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu" ,
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                

HELPER.update({
    "pro_noob": "\
**Available commands in pro_noob**\
\n\n`.younoob`\
\n`.menoob`\
\n`.youpro`\
\n`.mepro`\
"
})           
