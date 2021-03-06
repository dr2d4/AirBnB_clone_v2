#!/usr/bin/python3
# Create compress file with fabric
from fabric.api import *
import time


def do_pack():
    time_stamp = time.strftime("%Y%m%d%H%M%S")
    print(time_stamp)

    local("mkdir -p versions")
    local("tar czvf versions/web_static_{}.tgz web_static/".format(time_stamp))

    return "versions/web_static_{}.tgz".format(time_stamp)
