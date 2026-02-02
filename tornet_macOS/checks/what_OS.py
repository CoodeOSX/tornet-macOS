import platform

from tornet_macOS.messages.error import error


def what_OS():
    system = platform.system()
    # system = "Unix"
    try:
        return system
    except Exception as e:
        error(f"Unknown OS detecting Error: unsupported OS {e}")
