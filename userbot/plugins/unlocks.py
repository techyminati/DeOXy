# For The-TG-Bot-3.0
# By Priyam Kalra

import os
from global_variables_sql import SYNTAX, MODULE_LIST

MODULE_LIST.append("unlocks")

@borg.on(command(func=lambda e: e.is_group))
async def watch(event):
    if str(event.chat_id) not in str(Var.UNLOCKED_CHATS):
        return
    if not os.path.isdir(Var.DOWNLOAD_DIRECTORY):
        os.makedirs(Var.DOWNLOAD_DIRECTORY)
    if event.sticker:
        reply = await event.get_reply_message()
        file = event.sticker
        file_name = "sticker.png"
        to_download_directory = Var.DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await bot.download_media(
            file,
            downloaded_file_name
        )
        if os.path.exists(downloaded_file_name):
            await bot.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=reply,
            )
            os.remove(downloaded_file_name)

syntax.update({
    "unlocks": "\
Usage: Worksaround userbot/tg bot \"admin-only\" locks in chats.\
\nWhat can be sent in chats where its locked (for now):\
\n- stickers (only if sending pictures is allowed)\
\n\nYou need to add a chat to `UNLOCKED_CHATS` enviroment variables for this to take effect in those chats.\
"
})
