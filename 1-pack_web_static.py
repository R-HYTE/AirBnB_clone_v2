#!/usr/bin/python3
"""
This module defines a Fabric script for packing the contents of the web_static
folder into a .tgz archive. The main function, do_pack(), generates an archive
filename based on the current timestamp and compresses the web_static contents.

Functions:
    do_pack(): Generates a .tgz archive, returns the archive path if successful
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if successful, None otherwise.
    """
    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive filename using the current timestamp
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Compress the contents of the web_static folder into the archive
    try:
        local("tar -cvzf versions/{} web_static".format(archive_name))
        print("web_static packed: versions/{}".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Packaging failed:", str(e))
        return None
