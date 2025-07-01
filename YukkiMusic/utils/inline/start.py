#
# Copyright (C) 2024-2025 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#
import config
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP,CHANNEL_LINK
from YukkiMusic import app

Lnk= "https://t.me/" +config.CHANNEL_LINK
def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                callback_data="zzzback",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if CHANNEL_LINK:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=config.CHANNEL_NAME,
                    url=Lnk
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="قناة البوت",
                        url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: bool | int = None):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_1"], callback_data="zzzback")]
    ]
    if CHANNEL_LINK:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=config.CHANNEL_NAME,
                    url=Lnk
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="قناة البوت",
                        url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if OWNER:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_7"],
                    user_id=OWNER
                ),
            ]
        )
    
    return buttons
