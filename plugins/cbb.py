# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import CHANNEL, GROUP, OWNER
from Data import Data


@Bot.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.ABOUT.format(client.username, OWNER),
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
                text=Data.ABOUT.format(OWNER),
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
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
