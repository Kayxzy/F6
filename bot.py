# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        username = usr_bot_me.username
        namebot = usr_bot_me.first_name
        
        self.LOGGER(__name__).info(
            f"TG_BOT_TOKEN detected!\n┌ First Name: {namebot}\n└ Username: @{username}\n——"
        )

        if FORCE_SUB_1:
            try:
                var = "FORCE_SUB_1"
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Silakan tambahkan @{namebot} ke {var} dan Pastikan @{namebot} adalah Admin di Channel Tersebut, Chat ID Saat Ini: {info.id}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_2:
            try:
                var = "FORCE_SUB_2"
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Silakan tambahkan @{namebot} ke {var} dan Pastikan @{namebot} adalah Admin di Channel Tersebut, Chat ID Saat Ini: {info.id}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_3:
            try:
                var = "FORCE_SUB_3"
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_3)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Silakan tambahkan @{namebot} ke {var} dan Pastikan @{namebot} adalah Admin di Channel Tersebut, Chat ID Saat Ini: {info.id}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_4:
            try:
                var = "FORCE_SUB_4"
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Silakan tambahkan @{namebot} ke {var} dan Pastikan @{namebot} adalah Admin di Channel Tersebut, Chat ID Saat Ini: {info.id}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        try:
            var = "CHANNEL_ID"
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"{var} Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai {var}, Nilai Saat Ini: {db_channel.id}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
