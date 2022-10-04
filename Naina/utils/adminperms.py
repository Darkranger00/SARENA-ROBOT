import asyncio
from pyrogram import filters
from pyrogram.types import ChatPermissions, Message
from Naina import pbot as app


async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = await app.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms

def user_admin(permission: member_permissions):
    def wrapper(func):
        @functools.wraps(func)
        def awrapper(update: Update, context: CallbackContext, *args, **kwargs):
            nonlocal permission
            if update.effective_chat.type == "private":
                return func(update, context, *args, **kwargs)
            message = update.effective_message
            is_anon = bool(update.effective_message.sender_chat)

            if is_anon:
                callback_id = (
                    f"anoncb/{message.chat.id}/{message.message_id}/{permission.value}"
                )
                anon_callbacks[(message.chat.id, message.message_id)] = (
                    (update, context),
                    func,
                )
                anon_callback_messages[(message.chat.id, message.message_id)] = (
                    message.reply_text(
                        "Seems like you're anonymous, click the button below to prove your identity",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="Prove identity", callback_data=callback_id
                                    )
                                ]
                            ]
                        ),
                    )
                ).message_id
                # send message with callback f'anoncb{callback_id}'
            else:
                user_id = message.from_user.id
                chat_id = message.chat.id
                mem = context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
                if (
                    getattr(mem, permission.value) is True
                    or mem.status == "creator"
                    or user_id in DRAGONS
                ):
                    return func(update, context, *args, **kwargs)
                else:
                    return message.reply_text(
                        f"You lack the permission: `{permission.name}`",
                        parse_mode=ParseMode.MARKDOWN,
                    )

        return awrapper

    return wrapper
