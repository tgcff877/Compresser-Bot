#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hai, \n\n<code>Iam a simple telegram compresser bot. Send me any telegram file or media I Will compress without changing video quality</code>\n\n<code>For More Details Press</code> /help\n\n👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : @BX_Botz"
   
    ABS_TEXT = " Please don't be selfish 😌"
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "**DownloadinG 📥**"
    
    UPLOAD_START = "**UploadinG 📤**"
    
    COMPRESS_START = "📀 bTrying to compress ... "
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\n<b>Made With ❤️ By @BX_Botz</b>"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "**✅ Thumbnail Saved Successfully**"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "**✅ Thumbnail Cleared Succesfully**"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "**✅ Media Cleared Succesfully**"
    
    SAVED_RECVD_DOC_FILE = "**✅ Downloaded Successfully**"
    
    CUSTOM_CAPTION_UL_FILE = "**Made With ❤ By @BX_Botz**"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found 😔"
    
    NO_VOID_FORMAT_FOUND = "No Formats Found 😔\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "➠ <code>Send Me Any Media Or File</code>\n\n➠ <code>Reply To Telegram Media</code> /Compress\n\n<b>Made With ❤ By @BX_Botz</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
