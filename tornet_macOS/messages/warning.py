red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"


def warning(msg: str):
    """Print warning message"""
    print(f"{white} [{red}!{white}] {red}{msg}{reset}")
