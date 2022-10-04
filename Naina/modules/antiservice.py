from pyrogram import filters

from Naina import pbot as app
from Naina.utils.dbfunctions import antiservice_off, antiservice_on, is_antiservice_on
from Naina.utils.permissions import adminsOnly

__mod_name__ = "𝙰-ꜱᴇʀᴠ"
__help__ = """
ᴘʟᴜɢɪɴ ᴛᴏ ᴅᴇʟᴇᴛᴇ ꜱᴇʀᴠɪᴄᴇ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀ ᴄʜᴀᴛ!

/antiservice [ᴇɴᴀʙʟᴇ|ᴅɪꜱᴀʙʟᴇ]
"""


@app.on_message(filters.command("antiservice") & ~filters.private)
@adminsOnly("can_change_info")
async def anti_service(_, message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /antiservice [enable | disable]")
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await antiservice_on(chat_id)
        await message.reply_text(
            "Enabled AntiService System. I will Delete Service Messages from Now on."
        )
    elif status == "disable":
        await antiservice_off(chat_id)
        await message.reply_text(
            "Disabled AntiService System. I won't Be Deleting Service Message from Now on."
        )
    else:
        await message.reply_text("Unknown Suffix, Use /antiservice [enable|disable]")


@app.on_message(filters.service, group=11)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await is_antiservice_on(chat_id):
            return await message.delete()
    except Exception:
        pass
