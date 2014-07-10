# coding=utf-8

import hipchat
from django.conf import settings


def notify_hipchat(msg):
    hipster = hipchat.HipChat(token=settings.get('HIPCHAT_TOKEN'))
    hipster.message_room(
        settings.get('HIPCHAT_ROOM'),
        settings.get('HIPCHAT_NAME'),
        msg,
        color=settings.get('HIPCHAT_COLOR')
    )
