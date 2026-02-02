green = "\033[92m"
white = "\033[97m"
reset = "\033[0m"


def log(msg: str):
    """Print info message"""
    print(f"{white} [{green}+{white}]{green} {msg}{reset}")
