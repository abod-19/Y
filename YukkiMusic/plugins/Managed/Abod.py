import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import config
from config import BOT_NAME
from strings.filters import command
from YukkiMusic import app

# إعداد الرابط والاسم
lnk = "https://t.me/" + config.CHANNEL_LINK
Nb = BOT_NAME + " غنيلي"

# غنيلي
@app.on_message(filters.regex(rf"^(غنيلي|‹ غنيلي ›|{Nb})$"))
async def send_song(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/BE_19/{rl}"
    await client.send_voice(
        chat_id=message.chat.id,
        voice=url,
        caption="🤍",
        reply_to_message_id=message.id,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# صور
@app.on_message(command(["‹ صور ›", "صور"]) & filters.private)
async def send_image(client: Client, message: Message):
    rl = random.randint(2, 50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار صوره اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# انمي
@app.on_message(command(["‹ انمي ›", "انمي"]) & filters.private)
async def send_anime(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار انمي اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# متحركة
@app.on_message(command(["‹ متحركه ›", "متحركه"]) & filters.private)
async def send_gif(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(
        message.chat.id, url, caption="↯ : تم اختيار المتحركه اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# اقتباسات
@app.on_message(command(["‹ اقتباسات ›", "اقتباسات"]) & filters.private)
async def send_quote(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار اقتباس اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# هيدرات
@app.on_message(command(["هيدرات", "‹ هيدرات ›"]) & filters.private)
async def send_headers(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار هيدرات اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# افتارات شباب
@app.on_message(command(["‹ افتارات شباب ›"]) & filters.private)
async def send_boy_avatar(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/QrQsQ/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار صوره اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# افتارات بنات
@app.on_message(command(["‹ افتار بنات ›"]) & filters.private)
async def send_girl_avatar(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(
        message.chat.id, url, caption="↯ : تم اختيار صوره اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )

# قرآن
@app.on_message(command(["‹ قران ›", "قران"]) & filters.private)
async def send_quran(client: Client, message: Message):
    rl = random.randint(1, 90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(
        message.chat.id, url, caption="↯ : تم اختيار ايـه قرآنيه اليك",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=config.CHANNEL_NAME, url=lnk)]]
        )
    )
