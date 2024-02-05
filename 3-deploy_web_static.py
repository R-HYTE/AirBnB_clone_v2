#!/usr/bin/python3

"""
This module defines a Fabric script for deploying an archive to web servers.
The main function, deploy(), generates an archive using do_pack() and
deploys it using do_deploy().

Functions:
    deploy(): Generates and deploys an archive to web servers.
"""

from fabric.api import *
from datetime import datetime
from os.path import exists
import os

env.hosts = ['54.172.171.23', '54.172.83.49']  # <IP web-01>, <IP web-02>


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if successful, None otherwise.
    """
    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"

    # Compress the contents of the web_static folder into the archive
    try:
        local(f"tar -cvzf versions/{archive_name} web_static")
        print("web_static packed: versions/{}".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Packaging failed:", str(e))
        return None


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

    except Exception as e:
        print(e)
        return False


def deploy():
    """
    Generates and deploys an archive to web servers.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Generate the archive
    archive_path = do_pack()

    if archive_path is None:
        return False

    # Deploy the archive
    return do_deploy(archive_path)
