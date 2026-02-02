import sys

from tornet_macOS.messages.error import error
from tornet_macOS.messages.log import log
from tornet_macOS.run_cmd import run_cmd

from .ensure_pip import ensure_pip


def ensure_requests():
    """Ensure requests package is available"""
    try:
        import requests

        return True
    except ImportError:
        ensure_pip()
        log("requests package not found, installing...")
        try:
            run_cmd(
                [sys.executable, "-m", "pip", "install", "requests", "requests[socks]"]
            )  # ?
            return True
        except:
            error("Failed to install requests package.", 6)
