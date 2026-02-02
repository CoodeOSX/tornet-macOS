import shutil


def has_sudo():
    """Check if sudo is available"""
    return shutil.which("sudo") is not None
