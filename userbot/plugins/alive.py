from telethon import __version__


@client.on(events(pattern="alive"))
async def amireallyalive(event):
    me = await client.get_me()
    user = Var.ALIVE_NAME if Var.ALIVE_NAME else f"[{me.first_name}](tg://user?id={me.id})"

    info = f"•´¯``•.¸¸.•` 𝔡𝓔𝐎𝕩𝕐 `•.¸¸.•´´¯`•\
    \n\n👍🏻  `-̷-̷ Currently Alive! 🍻 -̷-̷` \
    \n\n__Telethon version: {__version__} // Python: 3.7.3__\
    \n\n**◆ ---------------- ✪ ----------------◆**\
    \n𝓑𝓸𝓽 𝓜𝓪𝓭𝓮 𝓑𝔂: [ᴊᴀɪꜱʜɴᴀᴠᴘʀᴀꜱᴀᴅ | #𝓣𝓱𝓮𝓣𝓮𝓬𝓱𝓖𝓪𝓷𝓰](t.me/CyberJalagam)\
    \nℱÃ𝐈𝕥н𝒻𝕦l𝕝𝔂 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑓𝑜𝑟: {user}\
    \n**◆ ---------------- ✪ ----------------◆**\
    \n\n                  ★彡 [GitHub](https://github.com/CyberJalagam/DeOXy) 彡★"
    
    await client.send_message(
        event.chat_id, 
        info, 
        file="logo.png", 
        force_document=False, 
        silent=True
    )
    await event.delete()


HELPER.update({"alive": "\
Available commands in **alive** module:\
\n\n`.alive`\
\nUsage: Checks if Userbot is alive.\
"})
