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
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
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

        if FORCE_SUB_CHANNEL:
            try:
                info = (await self.get_chat(FORCE_SUB_CHANNEL)).first_name
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_CHANNEL detected!\n┌ First Name: {info}\n└ Chat ID: {FORCE_SUB_CHANNEL}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL dan Pastikan Bot anda Admin di Channel Tersebut dengan izin link invite Pengguna melalui link undangan, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_GROUP:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP dan Pastikan Bot anda Admin di Group Tersebut dengan izin link invite Pengguna melalui link undangan, Chat ID F-Subs Group Saat Ini: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
