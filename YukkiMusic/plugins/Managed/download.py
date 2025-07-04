import random
import glob
import os
import re
import requests
import config
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from YukkiMusic import app
from YukkiMusic.plugins.play.filters import command
from YukkiMusic.core.mongo import mongodb

# استخراج ملف كوكيز عشوائي من مجلد cookies
def cookies():
    folder_path = f"{os.getcwd()}/config/cookies"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    return random.choice(txt_files)

# حذف ملف إذا كان موجوداً
def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)

songdb = mongodb.song
lnk = f"https://t.me/{config.CHANNEL_LINK}"
Nem = f"{config.BOT_NAME} ابحث"
Nam = f"{config.BOT_NAME} بحث"

@app.on_message(command(["song", "/song", "بحث", Nem, Nam, "يوت"]))
async def song_downloader(client, message: Message):
    if message.text.lower() in ["song", "/song", "بحث", Nem.lower(), Nam.lower(), "يوت"]:
        return

    # استخراج نص البحث
    if message.command[0] in config.BOT_NAME:
        query = " ".join(message.command[2:])
    else:
        query = " ".join(message.command[1:])
    
    m = await message.reply_text("<b>جـارِ البحث 🎵</b>")

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            await m.edit("- لم يتم العثور على نتائج، حاول مجددًا.")
            return

        video_id = results[0]['id']
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        title_clean = re.sub(r'[\\/*?:"<>|]', "", title)
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title_clean}.jpg"
        duration = results[0].get("duration", "0:00")

        # تحقق إن كان الفيديو موجود مسبقًا في قاعدة البيانات
        existing_entry = await songdb.find_one({"video_id": video_id})
        if existing_entry:
            channel_link = existing_entry["channel_link"]
            await client.send_voice(
                chat_id=message.chat.id,
                voice=channel_link,
                caption=f"⟡ <a href='{lnk}'>{app.name}</a>\nㅤ",
                reply_to_message_id=message.id,
            )
            await m.delete()
            return

        # تحميل الصورة المصغرة مع timeout
        try:
            thumb = requests.get(thumbnail, allow_redirects=True, timeout=10)
            open(thumb_name, "wb").write(thumb.content)
        except Exception as e:
            print("خطأ في تحميل الصورة المصغرة:", str(e))
            thumb_name = None

    except Exception as e:
        await m.edit("- لم يتم العثور على نتائج أو حدث خطأ أثناء البحث.")
        print(str(e))
        return

    await m.edit("<b>جاري التحميل 🎧</b>")

    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "keepvideo": False,
        "geo_bypass": True,
        "noplaylist": True,
        "nocheckcertificate": True,
        "no_warnings": True,
        "outtmpl": f"{title_clean}.%(ext)s",
        "quiet": True,
        "cookiefile": f"{cookies()}",
        "prefer_ffmpeg": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)

        # تحويل مدة الفيديو إلى ثوانٍ
        duration_parts = list(map(int, duration.split(":")))
        duration_in_seconds = sum(x * 60 ** i for i, x in enumerate(reversed(duration_parts)))

        await m.delete()
        await message.reply_audio(
            audio=audio_file,
            caption=f"⟡ <a href='{lnk}'>{app.name}</a>\nㅤ",
            title=title,
            performer=info_dict.get("uploader", "Unknown"),
            thumb=thumb_name,
            duration=duration_in_seconds,
        )

        # إرسال نسخة إلى القناة
        message_to_channel = await app.send_audio(
            chat_id="@IC_l9",
            audio=audio_file,
            caption=video_id,
            title=title,
            performer=info_dict.get("uploader", "Unknown"),
            thumb=thumb_name,
            duration=duration_in_seconds,
        )

        # حفظ الرابط في قاعدة البيانات
        await songdb.insert_one({
            "video_id": video_id,
            "channel_link": message_to_channel.link
        })

    except Exception as e:
        await m.edit("- تعذر تحميل أو رفع الملف الصوتي.")
        try:
            dev_id = 5145609515
            usr = await client.get_users(dev_id)
            usrnam = usr.username
            await app.send_message(
                chat_id=f"@{usrnam}",
                text=f"خطأ تحميل: {str(e)}"
            )
        except Exception as x:
            print("فشل إرسال رسالة للمطور:", x)
        print("خطأ أثناء التحميل:", e)

    # تنظيف الملفات المؤقتة
    try:
        if "audio_file" in locals():
            remove_if_exists(audio_file)
        if "thumb_name" in locals() and thumb_name:
            remove_if_exists(thumb_name)
    except Exception as e:
        print("خطأ في الحذف:", e)
