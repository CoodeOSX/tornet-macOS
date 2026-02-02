from tornet_macOS.checks.is_tor_installed import is_tor_installed
from tornet_macOS.messages.error import error
from tornet_macOS.messages.log import log

from .install_package import install_package


def ensure_tor():
    """Ensure tor is installed"""
    if is_tor_installed():
        return True

    log("tor not found, installing...")
    try:
        install_package("tor")
        return True
    except:
        error("Failed to install tor. Please install tor manually.", 7)
