#!/usr/bin/python3
# Deploy servers with Fabric
from fabric.operations import put, run, sudo
from fabric.api import *
import os.path
import time

env.hosts = ['35.237.192.177', '35.243.249.129']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
        Deploy server
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        file_ext = archive_path.split("/")[-1]
        file = '/data/web_static/releases/{}'.format(file_ext.split(".")[0])
        put(archive_path, "/tmp")

        run("mkdir -p {}".format(file))

        run("tar -xzf /tmp/{} -C {}/".format(file_ext, file))
        run("rm /tmp/{}".format(file_ext))

        run("mv {0}/web_static/* {0}".format(file))
        run("rm -rf {}/web_static".format(file))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(file))
        return True
    except:
        return False
