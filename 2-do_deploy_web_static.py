#!/usr/bin/python3
"""
This module defines a Fabric script for deploying an archive to web servers.
The main function, do_deploy(), uploads the archive, uncompresses it, and
updates the symbolic link to the new version on the web server.

Functions:
    do_deploy(archive_path): Deploys an archive to web servers.
"""

from fabric.api import run, put, env
from os.path import exists
import os

# <IP web-01>, <IP web-02>
env.hosts = ['54.172.171.23', '54.172.83.49']


def do_deploy(archive_path):
    """
    Deploy an archive to web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if successful, False otherwise.
    """

    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<file>
        archive_filename = os.path.basename(archive_path)
        release_folder = f"/data/web_static/releases/{archive_filename[:-4]}"
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents to the correct folder and clean up
        run("mv {}/web_static/* {}".format(release_folder, release_folder))
        run("rm -rf {}/web_static".format(release_folder))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
