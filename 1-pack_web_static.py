#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the
 contents of the web_static folder of your AirBnB Clone repo,
 using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    file_1 = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if file_1.failed:
        return None
    return file_1
