import importlib.metadata

from tornet_macOS.messages.log import log
from tornet_macOS.messages.warning import warning


def is_pip_installed():
    try:
        # Получаем версию пакета 'pip'
        version = importlib.metadata.version("pip")
        log(f"pip is already installed, pip version: {version}")
        return True
    except importlib.metadata.PackageNotFoundError:
        warning("pip not found")
        return False
