import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"⚠️ فایل بالا بعد از 30 ثانیه حذف خواهد شد !\n"
            f"➖ سریعا فایل را share کنید.\n"
            f"📥 [برای دریافت مجدد فایل کلیک کنید.](https://t.me/{Config.BOT_USERNAME}?start=HotLandXD_{str_to_b64(str(file_id))})\n\n"
            f"✨ @HotLandXD",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return media_forward(bot, user_id, file_id)

async def del_in(messages: Message):
    await asyncio.sleep(30)
    for msg in message:
        try:
            await msg.delete()
        except:
            pass

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await del_in([message, sent_message])
    await asyncio.sleep(2)
