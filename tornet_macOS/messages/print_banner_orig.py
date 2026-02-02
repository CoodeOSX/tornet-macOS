green = "\033[92m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"
cyan = "\033[36m"

TOOL_NAME = "tornet-macOS"
VERSION = "2.2.1"


def print_banner():
    """Print tool banner"""
    banner = f"""
{green}
   ████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗████████╗
   ╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
      ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║
      ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝     ██║
      ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║
      ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝
{white}                      Version: {VERSION}
{white} +---------------------{cyan}({red}ByteBreach{cyan}){white}---------------------+{reset}
{white} +--------------{cyan}({red}Improved by Ayad Seghiri{cyan}){white}--------------+{reset}
{white} +----{cyan}({red}Adaptation for macOS and {cyan}IP info {red}by {white}CoodeOSX{cyan}){white}----+{reset}
{reset}"""
    print(banner)
