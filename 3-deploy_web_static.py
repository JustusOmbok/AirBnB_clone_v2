#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) 
that creates and distributes an archive to your web servers, 
using the function deploy
"""
from fabric.api import run, local, env
from datetime import datetime
from os.path import exists

env.hosts = ["18.209.223.53", "54.160.76.99"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_pack():
    """ Generates a .tgz archive """
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None

def do_deploy(archive_path):

    """ An archive is distributed to web_servers and deployed """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        release_folder = "/data/web_static/releases/web_static_{}/".format(timestamp)
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_path.split("/")[-1], release_folder))
        run("rm /tmp/{}".format(archive_path.split("/")[-1]))
        run("mv {}web_static/* {}".format(release_folder, release_folder))
        run("rm -rf {}web_static".format(release_folder))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        return False

def deploy():
    """
    Deploys web_static content to web_servers
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
