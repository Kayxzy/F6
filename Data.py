# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

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
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:
{} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Simple dan Mudah!
 • Group Support: @SharingUserbot
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Language: <a href='https://www.python.org'>Python</a></b>
"""
