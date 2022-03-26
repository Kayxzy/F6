# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
✨ <b>Perintah Yang Tersedia

 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /ping  - untuk mengecek bot hidup
 × /users - untuk melihat statistik pengguna bot
 × /batch - untuk membuat link lebih dari satu file
 × /broadcast - untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by @Lunatic0de</b>
"""

    close = [
        [InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]
    ]

    buttons = [
        [
            InlineKeyboardButton("• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")
        ],
    ]

    ABOUT = f"""
<b>Tentang Bot ini:

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus

 • Creator:</b> [Klik Disini](tg://user?id={OWNER_ID})
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Language: <a href='https://www.python.org'>Python</a>

👨‍💻 Develoved by @Lunatic0de
"""
