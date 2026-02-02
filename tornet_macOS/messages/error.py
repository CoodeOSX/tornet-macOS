import sys

red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"


def error(msg: str, exit_code: int = 1):
    """Print error message and optionally exit"""
    print(f"{white} [{red}!{white}] {red}{msg}: Error =", exit_code, f"{reset}")
    if exit_code > 0:
        sys.exit(exit_code)
