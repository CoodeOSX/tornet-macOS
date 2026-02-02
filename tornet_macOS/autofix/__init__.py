from .auto_fix import auto_fix
from .detect_package_manager import detect_package_manager
from .ensure_pip import ensure_pip
from .ensure_requests import ensure_requests
from .ensure_tor import ensure_tor
from .install_package import install_package
from .is_pip_installed import is_pip_installed

__all__ = [
    "auto_fix",
    "detect_package_manager",
    "ensure_pip",
    "ensure_requests",
    "ensure_tor",
    "install_package",
    "is_pip_installed",
]
