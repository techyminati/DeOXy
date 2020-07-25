# For The-TG-Bot-3.0
# By Priyam Kalra
# Test_Port_DeOXy


import os


@borg.on(command(func=lambda e: e.is_group))
async def watch(event):
    if str(event.chat_id) not in str(Config.UNLOCKED_CHATS):
        return
    if not os.path.isdir(Config.DOWNLOAD_DIRECTORY):
        os.makedirs(Config.DOWNLOAD_DIRECTORY)
    if event.sticker:
        reply = await event.get_reply_message()
        file = event.sticker
        file_name = "sticker.png"
        to_download_directory = Config.DOWNLOAD_DIRECTORY
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
   
