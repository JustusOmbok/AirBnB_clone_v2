#!/usr/bin/python3
""" Uses fabric to generate a .tgz archive from the web static contents """

from fabric.api import local
from datetime import datetime


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
