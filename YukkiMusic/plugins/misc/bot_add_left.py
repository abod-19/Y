# All rights reserved.
#
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from YukkiMusic.utils.database import get_served_chats
from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import (
    delete_served_chat,
    get_assistant,
    is_on_off,
)

photo_urls = [
    "https://envs.sh/Wi_.jpg",
    "https://envs.sh/Wi_.jpg",
    "https://envs.sh/Wi_.jpg",
    "https://envs.sh/Wi_.jpg",
    "https://envs.sh/Wi_.jpg",
]

@app.on_message(filters.new_chat_members)
async def on_bot_added(_, message):
    served_chats = len(await get_served_chats())
    try:
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
                )
                msg = (
                    f"🌹 تمت إضافة البوت إلى مجموعة جديدة.\n\n"
                    f"┏━━━━━━━━━━━━━━━━━┓\n"
                    f"┣★ <b>𝙲𝙷𝙰𝚃</b> › : {message.chat.title}\n"
                    f"┣★ <b>𝙲𝙷𝙰𝚃 𝙸𝙳</b> › : {message.chat.id}\n"
                    f"┣★ <b>𝙲𝙷𝙰𝚃 𝚄𝙽𝙰𝙼𝙴</b> › : @{username}\n"
                    f"┣★ <b>𝙲𝙾𝚄𝙽𝚃</b> › : {count}\n"
                    f"┣★ <b>𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂</b> › : {served_chats}\n"
                    f"┗━━━ꪜ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo_urls),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=f"{message.from_user.first_name}",
                                    user_id=message.from_user.id,
                                )
                            ]
                        ]
                    ),
                )
                
    except Exception as e:
        await app.send_message(
            chat_id=5145609515,
            text=f"- حدث خطأ :\n{e}"
        )


@app.on_message(filters.left_chat_member)
async def on_bot_kicked(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == app.id:
            remove_by = (
                message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            )
            chat_id = message.chat.id
            left = (
                f"✫ <b><u>ـ تم طرد البوت من المجموعه</u></b> :\n"
                f"**Chat Name**: {title}\n"
                f"**Chat Id**: {chat_id}\n"
                f"**Chat Username**: {username}\n"
                f"**Removed By**: {remove_by}"
            )

            await app.send_photo(
                LOG_GROUP_ID,
                photo=random.choice(photo_urls),
                caption=left,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=f"{message.from_user.first_name}",
                                user_id=message.from_user.id,
                            )
                        ]
                    ]
                ),
            )

            await delete_served_chat(chat_id)

            # ✅ تحقق إن كان userbot عضو قبل محاولة الخروج
            try:
                member = await userbot.get_chat_member(chat_id, userbot.me.id)
                if member:
                    await userbot.leave_chat(chat_id)
            except Exception:
                pass  # تجاهل الخطأ إن لم يكن عضوًا أو حدث استثناء
    except Exception as e:
        await app.send_message(
            chat_id=5145609515,
            text=f"- حدث خطأ :\n{e}"
        )
