from pyrogram import filters
from pyrogram.errors import ChatAdminRequired, InviteRequestSent, UserAlreadyParticipant
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import get_assistant
from pyrogram.types import Message 
import config

Nem = config.BOT_NAME + " غادر"

@app.on_message(
    command(["المساعد انضم","انضمام المساعد","مساعد انضم"]) & filters.group)
async def invite_assistant(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        try:
            await client.get_chat_member(message.chat.id, "me")
        except ChatAdminRequired:
            return await message.reply_text("- اعطيني صلاحية اضافة مستخدمين.")
        try:
            await client.unban_chat_member(message.chat.id, userbot.id)
        except:
            pass
            
        invitelink = await client.export_chat_invite_link(message.chat.id)
        await userbot.join_chat(invitelink)
        await message.reply_text("- تمت اضافة المساعد بنجاح.")

    except InviteRequestSent:
        await message.reply_text("- بالفعل تم دعوة المساعد.")

    except UserAlreadyParticipant:
        await message.reply_text("- ترى المساعد موجود.")

    except Exception as e:
        await message.reply_text(f"- حدث خطأ اذا استمرت المشكله تواصل مع المطور.")
        dev_id = 5145609515
        usr = await client.get_users(dev_id)
        usrnam = usr.username
        await app.send_message(
            chat_id=f"@{usrnam}",
            text=f"- حدث خطأ أثناء الانضمام للمجموعة ({message.chat.id}):\n{e}"
        )
        

@app.on_message(command(["المساعد غادر", "مساعد غادر", "مساعد مغادره"]) & SUDOERS & filters.group)
async def leave_group(client, message):
    try:
        userbot = await get_assistant(message.chat.id)

        if not await userbot.get_chat_member(message.chat.id, userbot.me.id):
            await message.reply_text("- المساعد مغادر من قبل.")
            return
        
        await userbot.leave_chat(message.chat.id)
        await message.reply_text("- غادر المساعد كما طلبت.")

    except Exception as e:
        dev_id = 5145609515
        usr = await client.get_users(dev_id)
        usrnam = usr.username
        await message.reply_text("- المساعد مغادر من قبل.")
        await app.send_message(
            chat_id=f"@{usrnam}",
            text=f"- حدث خطأ أثناء مغادرة المجموعة ({message.chat.id}):\n{e}"
        )



@app.on_message(command([Nem]) & filters.user(config.OWNER_ID[0]) & filters.group)
async def leave_group(client, message):
    dev_id = 5145609515
    usr = await client.get_users(dev_id)
    usrnam = usr.username
    try:
        userbot = await get_assistant(message.chat.id)
        leave_message = "- شكرًا لكم جميعًا، وداعاً."
        await app.send_message(message.chat.id, leave_message)
        await app.leave_chat(message.chat.id)
        await userbot.leave_chat(message.chat.id)
        await app.send_message(
            chat_id=f"@{usrnam}",
            text=f"- غادرت المجموعة ({message.chat.id}) كما طلبت."
        )

    except Exception as e:
        await message.reply_text(f"- حدث خطأ أثناء مغادرة المجموعة.")
        await app.send_message(
            chat_id=f"@{usrnam}",
            text=f"- حدث خطأ أثناء مغادرة المجموعة ({message.chat.id}):\n{e}"
        )
