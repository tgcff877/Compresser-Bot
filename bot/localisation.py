#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hai, \n\n𝙸𝚊𝚖  𝚊  𝚜𝚒𝚖𝚙𝚕𝚎  𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖  𝚟𝚒𝚍𝚎𝚘  𝚌𝚘𝚖𝚙𝚛𝚎𝚜𝚜𝚎𝚛  𝚋𝚘𝚝 . 𝚜𝚎𝚗𝚍  𝚖𝚎  𝚊𝚗𝚢  𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖  𝚏𝚒𝚕𝚎  𝚘𝚛  𝚖𝚎𝚍𝚒𝚊 . 𝙸  𝚠𝚒𝚕𝚕  𝚌𝚘𝚖𝚙𝚛𝚎𝚜𝚜  𝚒𝚝\n\n𝙵𝚘𝚛  𝚖𝚘𝚛𝚎  𝚍𝚎𝚝𝚊𝚒𝚕𝚜  𝚙𝚛𝚎𝚜𝚜 /help.\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading ... 📥 \n"
    
    UPLOAD_START = "📤 Uploading ... 📤 \n"
    
    COMPRESS_START = "📀 Trying to compress ... 📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\nBy @Discovery_Updates"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "➠ Send Me Any Media Or File\n\n➠ Reply To Telegram Media /Compress"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
