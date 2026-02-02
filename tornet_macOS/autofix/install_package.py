from tornet_macOS.messages.error import error
from tornet_macOS.run_cmd import run_cmd

from .detect_package_manager import detect_package_manager


def install_package(package_name):
    """Install system package using detected package manager"""
    pm = detect_package_manager()
    if not pm:
        error(
            "No supported package manager found. Please install packages manually.", 4
        )

    if pm == "apt":
        run_cmd(["apt-get", "update"], use_sudo=True)
        run_cmd(["apt-get", "install", "-y", package_name], use_sudo=True)
    elif pm == "dnf":
        run_cmd(["dnf", "install", "-y", package_name], use_sudo=True)
    elif pm == "yum":
        run_cmd(["yum", "install", "-y", package_name], use_sudo=True)
    elif pm == "pacman":
        run_cmd(["pacman", "-Sy", "--noconfirm", package_name], use_sudo=True)
    elif pm == "apk":
        run_cmd(["apk", "add", package_name], use_sudo=True)
    elif pm == "zypper":
        run_cmd(["zypper", "--non-interactive", "install", package_name], use_sudo=True)
    elif pm == "brew":
        run_cmd(["brew", "install", package_name], use_sudo=False)
