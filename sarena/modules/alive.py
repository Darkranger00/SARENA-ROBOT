import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from sarena.events import register
from sarena import telethn as tbot


PHOTO = "https://telegra.ph/file/0d96581fcc4b548fa5515.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜɪɪ [{event.sender.first_name}](tg://user?id={event.sender.id}),** \n\n"
    TEXT += "» **ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ** \n\n"
    TEXT += f"» **ᴍᴀʜ ᴏᴡɴᴇʀ : [𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ✘「ᴍʀ🇮🇳ʟᴜᴄᴋʏ」✘𑲭](https://t.me/cute_boy701)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{pyrover}` \n\n"
    TEXT += "**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ 💜**"
    BUTTON = [
        [
            Button.url("๏ ꜱᴜᴘᴘᴏʀᴛ ๏", "https://t.me/Lobe_ju"),
            Button.url("๏ ᴄʜᴀɴɴᴇʟ ๏", "https://t.me/oye_golgappu"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
