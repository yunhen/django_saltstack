# coding=utf-8

import hipchat
from django.conf import settings
import salt.config
import salt.runner
import salt.utils.event


def notify_hipchat(msg):
    hipster = hipchat.HipChat(token=settings.HIPCHAT_TOKEN)
    hipster.message_room(
        settings.HIPCHAT_ROOM,
        settings.HIPCHAT_NAME,
        msg,
        color=settings.HIPCHAT_COLOR
    )


def get_task_info(task_id):
    '''
    this function sometimes is blocking forever (probably when initializing the runner).
    Needs debugging.
    '''
    print "get config..."
    # opts = salt.config.master_config('/etc/salt/master')
    print "patch opts"
    opts = {
        'master_uri': 'tcp://localhost:4506/',
        'extension_modules': '/var/cache/salt/master/extmods',
    }
    print "init runner"
    runner = salt.runner.RunnerClient(opts)
    print "init event"
    event = salt.utils.event.MasterEvent('/var/run/salt/master')
    print "getting tag..."
    tag = runner.master_call(
        fun='jobs.lookup_jid',
        kwarg={'jid': str(task_id)},
        eauth='pam',
        username='django_saltstack',
        password=settings.USER_PASSWORD)['tag']
    print "get out1"
    out1 = event.get_event(wait=1, tag=tag)
    print out1
    print "get out2"
    out2 = event.get_event(wait=1, tag=tag)
    print out2
    event.unsubscribe()
    event.destroy()
    return '{}\n{}'.format(out1, out2)
