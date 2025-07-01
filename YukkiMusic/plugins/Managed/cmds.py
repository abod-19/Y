import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from YukkiMusic import app
from config import START_IMG_URL
import config
Lnk= "https://t.me/" +config.CHANNEL_LINK

@app.on_message(filters.regex(r"^(اوامر الميوزك|ميوزك|الاوامر|الميوزك|اوامر ميوزك)$"))
async def zdatsr(client: Client, message: Message):
    
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=f"""<b>- منور يحبي باوامر الميوزك .</b>\n<b>- استخدم الازرار الي تحت .\n- عشان تشوف اوامر الميوزك يعيني .</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامــر التشغيــل", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر القنـاة", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "اوامـر الادمـن", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "اوامــر المطــور", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=Lnk),
                ],
            ]
        ),
    )
