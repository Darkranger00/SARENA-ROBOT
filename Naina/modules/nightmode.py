import os
from Naina.modules.sql.night_mode_sql import (
    add_nightmode,
    rmnightmode,
    get_all_chat_id,
    is_nightmode_indb,
)
from telethon.tl.types import ChatBannedRights
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon import functions
from Naina.events import register
from Naina import telethn as tbot, OWNER_ID
from telethon import Button, custom, events

hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)

from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


async def can_change_info(message):
    result = await tbot(
        functions.channels.GetParticipantRequest(
            channel=message.chat_id,
            user_id=message.sender_id,
        )
    )
    p = result.participant
    return isinstance(p, types.ChannelParticipantCreator) or (
        isinstance(p, types.ChannelParticipantAdmin) and p.admin_rights.change_info
    )


@register(pattern="^/(nightmode|Nightmode|NightMode|kontolmode|KONTOLMODE) ?(.*)")
async def profanity(event):
    if event.fwd_from:
        return
    if event.is_private:
        return
    input = event.pattern_match.group(2)
    if not event.sender_id == OWNER_ID:
        if not await is_register_admin(event.input_chat, event.sender_id):
            await event.reply("Only admins can execute this command!")
            return
        else:
            if not await can_change_info(message=event):
                await event.reply(
                    "You are missing the following rights to use this command:CanChangeinfo"
                )
                return
    if not input:
        if is_nightmode_indb(str(event.chat_id)):
            await event.reply("ᴄᴜʀʀᴇɴᴛʟʏ ɴɪɢʜᴛᴍᴏᴅᴇ ᴅɪꜱᴀʙʟᴇᴅ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ.")
            return
        await event.reply("ᴄᴜʀʀᴇɴᴛʟʏ ɴɪɢʜᴛᴍᴏᴅᴇ ᴅɪꜱᴀʙʟᴇᴅ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ.")
        return
    if "on" in input:
        if event.is_group:
            if is_nightmode_indb(str(event.chat_id)):
                await event.reply("Nɪɢʜᴛᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ.")
                return
            add_nightmode(str(event.chat_id))
            await event.reply("ɴɪɢʜᴛᴍᴏᴅᴇ ᴛᴜʀɴᴇᴅ ᴏɴ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ.")
    if "off" in input:
        if event.is_group:
            if not is_nightmode_indb(str(event.chat_id)):
                await event.reply("ɴɪɢʜᴛᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴏꜰꜰ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ.")
                return
        rmnightmode(str(event.chat_id))
        await event.reply("NightMode Disabled!")
    if not "off" in input and not "on" in input:
        await event.reply("Please Specify On or Off!")
        return


async def job_close():
    chats = get_all_chat_id()
    if len(chats) == 0:
        return
    for pro in chats:
        try:
            await tbot.send_message(
                int(pro.chat_id),
                "12:00 ᴀᴍ, ɢʀᴏᴜᴘ ɪꜱ ᴄʟᴏꜱɪɴɢ ᴛɪʟʟ 6 ᴀᴍ. ɴɪɢʜᴛᴍᴏᴅᴇ ꜱᴛᴀʀᴛᴇᴅ ! \n**ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʟᴜᴄᴋʏ ʀᴏʙᴏᴛ**",
            )
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(pro.chat_id), banned_rights=hehes
                )
            )
        except Exception as e:
            logger.info(f"Unable To Close Group {chat} - {e}")


# Run everyday at 12am
scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=59)
scheduler.start()


async def job_open():
    chats = get_all_chat_id()
    if len(chats) == 0:
        return
    for pro in chats:
        try:
            await tbot.send_message(
                int(pro.chat_id),
                "06:00 ᴀᴍ, ɢʀᴏᴜᴘ ɪꜱ ᴏᴘᴇɴɪɴɢ.\n**Pᴏᴡᴇʀᴇᴅ ʙʏ ʟᴜᴄᴋʏ ʀᴏʙᴏᴛ**",
            )
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(pro.chat_id), banned_rights=openhehe
                )
            )
        except Exception as e:
            logger.info(f"Unable To Open Group {pro.chat_id} - {e}")


# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_open, trigger="cron", hour=5, minute=58)
scheduler.start()


__mod_name__ = "𝙽-ᴍᴏᴅᴇ"

__help__ = """
➻ /nightmode  : Aᴅᴅs Gʀᴏᴜᴘ ᴛᴏ NɪɢʜᴛMᴏᴅᴇ Cʜᴀᴛs

➻ /rmnight : Rᴇᴍᴏᴠᴇs Gʀᴏᴜᴘ Fʀᴏᴍ NɪɢʜᴛMᴏᴅᴇ Cʜᴀᴛs

*Nᴏᴛᴇ: Nɪɢʜᴛ Mᴏᴅᴇ ᴄʜᴀᴛs ɢᴇᴛ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴏsᴇᴅ ᴀᴛ 12 ᴀᴍ(IST) ᴀɴᴅ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴏᴘᴇɴɴᴇᴅ ᴀᴛ 6 ᴀᴍ(IST) ᴛᴏ Pʀᴇᴠᴇɴᴛ Nɪɢʜᴛ Sᴘᴀᴍs*
"""
