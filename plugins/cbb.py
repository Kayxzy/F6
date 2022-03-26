# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import CHANNEL, GROUP, OWNER_ID
from Data import Data


@Bot.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.ABOUT.format(OWNER_ID),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.close),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        "<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=f"<b>Tentang Bot ini:\n\nBot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus\n\n • Creator : <a href='tg://user?id={OWNER_ID}'>Klik Disini</a>\n • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>\n • Language: <a href='https://www.python.org'>Python</a>\n\n👨‍💻 Develoved by @Lunatic0de</b>",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.close),
            )
        except MessageNotModified:
            pass
    elif data == "help":
        try:
            chat_id = query.from_user.id
            message_id = query.message.message_id
            await query.message.edit_text(
                text=Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.close),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
