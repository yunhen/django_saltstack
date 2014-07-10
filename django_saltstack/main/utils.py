# coding=utf-8

import hipchat
from django.conf import settings


def notify_hipchat(msg):
    hipster = hipchat.HipChat(token=settings.HIPCHAT_TOKEN)
    hipster.message_room(
        settings.HIPCHAT_ROOM,
        settings.HIPCHAT_NAME,
        msg,
        color=settings.HIPCHAT_COLOR
    )
