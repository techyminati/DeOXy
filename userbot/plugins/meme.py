"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3
By : - @Zero_cool7870

"""
import asyncio
import os
import sys


@client.on(events(pattern="meme"))
async def meme(event):
    if event.fwd_from:
        return   
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:] 
           
    await event.edit("-------------"+memeVar)
    await event.edit("------------"+memeVar+"-")
    await event.edit("-----------"+memeVar+"--")
    await event.edit("----------"+memeVar+"---")
    await event.edit("---------"+memeVar+"----")    
    await event.edit("--------"+memeVar+"-----")
    await event.edit("-------"+memeVar+"------")
    await event.edit("------"+memeVar+"-------")
    await event.edit("-----"+memeVar+"--------")
    await event.edit("----"+memeVar+"---------")
    await event.edit("---"+memeVar+"----------")
    await event.edit("--"+memeVar+"-----------")
    await event.edit("-"+memeVar+"------------")
    await event.edit(memeVar+"-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

"""
@client.on(events(pattern="flower"))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 5
           
    await event.edit(flower+"        ")
    await event.edit(flower+flower+"       ")
    await event.edit(flower+flower+flower+"      ")
    await event.edit(flower+flower+flower+flower+"     ")
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
        
    


HELPER.update({"meme": "\
**Available commands in meme module:**\
\n`.meme`\
\n`.flower`\
"})
