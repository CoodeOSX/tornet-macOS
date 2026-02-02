from tornet_macOS.messages.log import log

from .ensure_pip import ensure_pip
from .ensure_requests import ensure_requests
from .ensure_tor import ensure_tor


def auto_fix():
    """Automatically fix dependencies"""
    log("Running auto-fix...")
    ensure_pip()
    ensure_requests()
    ensure_tor()
    log("Auto-fix complete")
