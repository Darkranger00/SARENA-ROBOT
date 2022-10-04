import os
import random
import glob
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telethon.tl.types import InputMessagesFilterPhotos
from telethon import events, Button, custom, version
from Naina.events import register
from Naina import telethn as tbot, ubot2


def mediainfo(media):
    xx = str((str(media)).split("(", maxsplit=1)[0])
    m = ""
    if xx == "MessageMediaDocument":
        mim = media.document.mime_type
        if mim == "application/x-tgsticker":
            m = "sticker animated"
        elif "image" in mim:
            if mim == "image/webp":
                m = "sticker"
            elif mim == "image/gif":
                m = "gif as doc"
            else:
                m = "pic as doc"
        elif "video" in mim:
            if "DocumentAttributeAnimated" in str(media):
                m = "gif"
            elif "DocumentAttributeVideo" in str(media):
                i = str(media.document.attributes[0])
                if "supports_streaming=True" in i:
                    m = "video"
                m = "video as doc"
            else:
                m = "video"
        elif "audio" in mim:
            m = "audio"
        else:
            m = "document"
    elif xx == "MessageMediaPhoto":
        m = "pic"
    elif xx == "MessageMediaWebPage":
        m = "web"
    return m


@register(pattern="^/logo ?(.*)")
async def logo_gen(event):
    xx = await event.reply("⟳ ᴍᴀᴋɪɴɢ ʏᴏᴜʀ ʟᴏɢᴏ ʙᴀʙʏ")
    name = event.pattern_match.group(1)
    if not name:
        await xx.edit("➻ ᴘʀᴏᴠɪᴅᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴅʀᴀᴡ ʙᴀʙʏ!")
        return
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in ubot2.iter_messages(
            "@KenLogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("./Naina/resources/fonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in ubot2.iter_messages(
            "@KenLogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("./Naina/resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 120
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 100
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), name, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    flnme = f"logo.png"
    img.save(flnme, "png")
    await xx.edit("➻ ᴜᴘʟᴏᴀᴅɪɴɢ ʙᴀʙʏ")
    if os.path.exists(flnme):
        await tbot.send_file(
            event.chat_id,
            file=flnme,
            caption="""
━━━━━━  ᴛᴇᴀᴍ ʟᴜᴄᴋʏ  ━━━━━━

◈──────────────◈
♦️ ᴄʀᴇᴀᴛᴇᴅ ʙʏ : [Lᴜᴄᴋʏ](https://t.me/lucky_officialbot)
♦️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [Tᴇᴀᴍ ʟᴜᴄᴋʏ](https://t.me/luckyxbots)
◈──────────────◈

━━━━━━  ᴛᴇᴀᴍ ʟᴜᴄᴋʏ  ━━━━━━
""",
            force_document=False,
        )
        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("./Naina/resources/fonts"):
            os.remove(font_)


@register(pattern="^/wlogo ?(.*)")
async def logo_(event):
    xx = await event.reply("⟳ ᴍᴀᴋɪɴɢ ʏᴏᴜʀ ʟᴏɢᴏ ʙᴀʙʏ")
    name = event.pattern_match.group(1)
    if not name:
        await xx.edit("➻ ᴘʀᴏᴠɪᴅᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴅʀᴀᴡ ʙᴀʙʏ!")
        return
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in ubot2.iter_messages(
            "@kenlogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("./Naina/resources/fonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in ubot2.iter_messages(
            "@kenlogopack", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("./Naina/resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 105
        strke = 8
    elif len(name) >= 9:
        fnt_size = 50
        strke = 4
    else:
        fnt_size = 95
        strke = 13
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), name, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    flnme = f"logo.png"
    img.save(flnme, "png")
    await xx.edit("➻ ᴜᴘʟᴏᴀᴅɪɴɢ ʙᴀʙʏ")
    if os.path.exists(flnme):
        await tbot.send_file(
            event.chat_id,
            file=flnme,
            caption="""
━━━━━━  ᴛᴇᴀᴍ ʟᴜᴄᴋʏ  ━━━━━━

◈──────────────◈
♦️ ᴄʀᴇᴀᴛᴇᴅ ʙʏ : [Lᴜᴄᴋʏ](https://t.me/lucky_officialbot)
♦️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [Tᴇᴀᴍ ʟᴜᴄᴋʏ](https://t.me/luckyxbots)
◈──────────────◈

━━━━━━  ᴛᴇᴀᴍ ʟᴜᴄᴋʏ  ━━━━━━
""",
            force_document=False,
        )
        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("./EmikoRobot/resources/fonts"):
            os.remove(font_)


__mod_name__ = "𝙻ᴏɢᴏꜱ"

__help__ = """ *ᴛʜɪꜱ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ғᴏʀ ʟᴏɢᴏᴍᴀᴋᴇʀ*

•➥ /logo <text/name> - ᴄʀᴇᴀᴛᴇ a ʟᴏɢᴏ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.

•➥ /wlogo <text/name> - ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ ᴡɪᴛʜ ᴡɪᴅᴇ ᴠɪᴇᴡ ᴏɴʟʏ.

•➥ /wallpaper - ɢᴇᴛ ᴀ ᴡᴀʟʟᴘᴀᴘᴇʀ 

 *ɪᴍᴀɢᴇ ᴇᴅɪᴛᴏʀ:*
•➥  /edit <reply photo> - ᴛᴏ ᴇᴅɪᴛ ɪᴍᴀɢᴇ.

*➻ ᴘᴏᴡᴇʀᴅ  ʙʏ © ɴᴀɪɴᴀ-✗ᴅ ™*
"""
