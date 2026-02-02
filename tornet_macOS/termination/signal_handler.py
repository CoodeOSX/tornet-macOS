import sys

from .stop_services import stop_services

red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"


def signal_handler(sig, frame):
    """Handle interrupt signals"""
    stop_services()
    print(f"\n{white} [{red}!{white}] {red}Program terminated by user.{reset}")
    sys.exit(0)


# signal_handler(2, None)
