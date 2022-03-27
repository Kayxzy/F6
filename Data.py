# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
✨ <b>Perintah untuk Pengguna BOT

 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /ping  - untuk mengecek bot hidup

✨ Perintah Untuk Admin BOT

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

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Language: <a href='https://www.python.org'>Python</a>

👨‍💻 Develoved by @Lunatic0de</b>
"""
