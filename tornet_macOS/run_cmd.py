import subprocess

from tornet_macOS.checks.has_sudo import has_sudo
from tornet_macOS.checks.is_root import is_root
from tornet_macOS.messages.error import error


def run_cmd(cmd, use_sudo=False, check=True):
    """Run command safely with optional sudo"""
    if use_sudo and not is_root():
        if not has_sudo():
            error(
                "Root privileges required but sudo not available. Run as root or install sudo.",
                2,
            )
        cmd = ["sudo"] + cmd

    try:
        result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        if check:
            error(f"Command failed: {' '.join(cmd)}\nError: {e.stderr.strip()}")
        return e
