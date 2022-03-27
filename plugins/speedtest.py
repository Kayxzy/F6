#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import os

import speedtest
import wget
from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("Running Download SpeedTest")
        test.download()
        m = m.edit("Running Upload SpeedTest")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("Sharing SpeedTest Results")
        path = wget.download(result["share"])
    except Exception as e:
        return m.edit(e)
    return result, path


@Bot.on_message(filters.command("speedtest") & filters.user(ADMINS))
async def speedtest_function(client: Bot, message: Message):
    m = await message.reply_text("Running Speed test")
    loop = asyncio.get_event_loop()
    result, path = await loop.run_in_executor(None, testspeed, m)
    output = f"""💡 **SpeedTest Results**
    
<u>**Client:**</u>
**ISP:** {result['client']['isp']}
**Country:** {result['client']['country']}
  
<u>**Server:**</u>
**Name:** {result['server']['name']}
**Country:** {result['server']['country']}, {result['server']['cc']}
**Sponsor:** {result['server']['sponsor']}
**Latency:** {result['server']['latency']}

⚡️ **Ping:** {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
