#!/usr/bin/python3i
"""
Script that deletes out-dated archives.
"""

from fabric.api import env, run, local, lcd, cd
from fabric.decorators import runs_once
from datetime import datetime
import os

env.hosts = ['18.209.223.53', '54.160.76.99']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"

remote_versions_path = '/data/web_static/releases'
local_versions_path = 'versions'


def do_clean(number=0):
    """
    Deletes out-dated archives from local and remote.
    """
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir(local_versions_path))
    archives_to_delete = archives[:-number]

    with lcd(local_versions_path):
        for archive in archives_to_delete:
            local("rm -f {}".format(archive))

    with cd(remote_versions_path):
        for archive in archives_to_delete:
            run("rm -f {}".format(archive))
