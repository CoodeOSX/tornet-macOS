import os

def is_root():
    """Check if running as root"""
    return os.geteuid() == 0
