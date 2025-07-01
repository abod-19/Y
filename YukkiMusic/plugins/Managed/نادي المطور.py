from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from strings.filters import command
from YukkiMusic import app
from config import OWNER_ID, BOT_NAME

Nem = BOT_NAME + " نادي المطور"

@app.on_message(filters.command(["نادي المطور", Nem], "") & filters.group)
async def call_dev(client: Client, message: Message):
    usm = await client.get_users(OWNER_ID[0])
    mname = usm.first_name
    musrnam = usm.username

    chat = message.chat
    gti = chat.title
    chatusername = f"@{chat.username}" if chat.username else "لا يوجد يوزر"

    link = await app.export_chat_invite_link(chat.id)

    user = message.from_user
    user_id = user.id
    user_ab = user.username or "بدون يوزر"
    user_name = user.first_name

    buttons = [[InlineKeyboardButton(gti, url=link)]]
    reply_markup = InlineKeyboardMarkup(buttons)

    await app.send_message(
        OWNER_ID[0],
        f"<b>⌯ قام {user.mention}\n"
        f"⌯ بمناداتك عزيزي المطور\n"
        f"⌯ الأيدي {user_id}\n"
        f"⌯ اليوزر @{user_ab}\n"
        f"⌯ ايدي المجموعة {chat.id}\n"
        f"⌯ يوزر المجموعه {chatusername}</b>",
        reply_markup=reply_markup,
    )

    await message.reply_text("- تم إرسال طلبك للمطور، سيتم الرد عليك قريباً.")
