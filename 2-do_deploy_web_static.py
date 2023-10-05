#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
That distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ["18.209.223.53", "54.160.76.99"]


def do_deploy(archive_path):
    """ An archive is distributed to web_servers and deployed """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        release_folder = "/data/web_static/releases/web_static_{}/"
        .format(timestamp)
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}"
            .format(archive_path.split("/")[-1], release_folder))
        run("rm /tmp/{}".format(archive_path.split("/")[-1]))
        run("mv {}web_static/* {}".format(release_folder, release_folder))
        run("rm -rf {}web_static".format(release_folder))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
