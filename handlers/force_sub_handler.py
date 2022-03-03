import asyncio
from typing import (
    Union
)
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def get_invite_link(bot: Client, chat_id: Union[str, int]):
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait ...")
        await asyncio.sleep(e.x)
        return await get_invite_link(bot, chat_id)


async def handle_force_sub(bot: Client, cmd: Message):
    if Config.UPDATES_CHANNEL:
        if type(Config.UPDATES_CHANNEL[0]) == int:
            channel_chat_id = int(Config.UPDATES_CHANNEL)
        elif type(Config.UPDATES_CHANNEL[0]) == str:
            channel_chat_id = Config.UPDATES_CHANNEL
    else:
        return 200
    try:
        user = await bot.get_chat_member(chat_id=channel_chat_id, user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="✨ شما به علت عدم رعایت قوانین از بات بن شده و دیگر نمیتوانید استفاده کنید!",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            for i in channel_chat_id:
                invite_link1 = await get_invite_link(bot, chat_id=i[0])
                invite_link2 = await get_invite_link(bot, chat_id=i[1])
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="✨ **لطفا در چنل های زیر جوین شده و پس از عضویت روی بررسی عضویت کلیک کنید!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔸1 عضویت در چنل 🔹", url=invite_link.invite_link1)
                    ],
                    [
                        InlineKeyboardButton("🔸2 عضویت در چنل 🔹", url=invite_link.invite_link2)
                    ],
                    [
                        InlineKeyboardButton("👁‍🗨 بررسی عضویت 👁‍🗨", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="خطایی رخ داده است. با پشتیبانی در تماس باشید",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 200
    return 200
