#!/usr/bin/python3
""" Fabric script for deploying an archive to web servers """

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['54.172.171.23', '54.172.83.49']  # <IP web-01>, <IP web-02>


def do_deploy(archive_path):
    """ Deploy an archive to web servers """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Extract archive to the folder /data/web_static/releases/<filename>
        filename = archive_path.split('/')[-1]
        release_folder = (
            "/data/web_static/releases/{}"
            .format(filename.split('.')[0])
        )

        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(filename, release_folder))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move the contents to the correct folder and clean up
        run("mv {}/web_static/* {}".format(release_folder, release_folder))
        run("rm -rf {}/web_static".format(release_folder))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True

    except:
        return False
