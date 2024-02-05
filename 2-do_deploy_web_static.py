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
        release_folder = f"/data/web_static/releases/{filename.split('.')[0]}"
        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf /tmp/{filename} -C {release_folder}")

        # Delete the archive from the web server
        run(f"rm /tmp/{filename}")

        # Move the contents to the correct folder and clean up
        run(f"mv {release_folder}/web_static/* {release_folder}")
        run(f"rm -rf {release_folder}/web_static")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_folder} /data/web_static/current")

        return True

    except Exception as e:
        print(e)
        return False
