# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
✨ <b>Perintah Yang Tersedia
 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /ping  - untuk mengecek bot
 × /users - lihat statistik pengguna bot
 × /batch - buat link untuk lebih dari satu file
 × /broadcast - menyiarkan/broadcast pesan apa pun ke pengguna bot

👨‍💻 Develoved by @mrismanaziz</b>
"""

    home_buttons = [
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ", callback_data="generate")]
    ]

    close = [
        [InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", url="https://t.me/Lunatic0de/63")]
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
