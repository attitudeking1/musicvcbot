from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("repo")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**VEDMAT:**  BOT DEVELOPER @VEDIC_MATHS_OWNER
WHO IS HE ? 
CHECK ABOUT HIM @ABOUT_VEDMAT_OWNER  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/attitudeking1/musicvcbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://repl.it/@attitudeking1/Musicbot2"
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fattitudeking1%2Fmusicvcbot&template=https%3A%2F%2Fgithub.com%2Fattitudeking1%2Fmusicvcbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
    
@Client.on_message(
    filters.command("repo")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        "**VEDMAT:** BOT DEVELOPER @VEDIC_MATHS_OWNER
WHO IS HE ? 
CHECK ABOUT HIM @ABOUT_VEDMAT_OWNER  \n**GO AND DEPLOY ❤️**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 REPO 💙", url="https://github.com/attitudeking1/musicvcbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💚 SESSION 💚", url="https://replit.com/@attitudeking1/Musicbot2 "
                    ),
                    InlineKeyboardButton(
                        "💜 HEROKU 💜", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fattitudeking1%2Fmusicvcbot&template=https%3A%2F%2Fgithub.com%2Fattitudeking1%2Fmusicvcbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
