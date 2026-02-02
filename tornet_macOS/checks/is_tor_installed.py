import shutil

def is_tor_installed():
    """Check if tor binary is installed"""
    return shutil.which("tor") is not None
