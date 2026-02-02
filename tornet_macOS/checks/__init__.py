from .check_internet_connection import check_internet_connection
from .detect_service_manager import detect_service_manager
from .has_sudo import has_sudo
from .is_root import is_root
from .is_tor_installed import is_tor_installed
from .is_tor_running import is_tor_running
from .what_OS import what_OS

__all__ = [
    "check_internet_connection",
    "detect_service_manager",
    "has_sudo",
    "is_root",
    "is_tor_installed",
    "is_tor_running",
    "what_OS",
]
