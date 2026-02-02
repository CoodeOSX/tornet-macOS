import importlib.resources

# import os
# import sys
# import pkg_resources
import requests

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../messages")))
# sys.path.append(os.path.join(os.path.dirname(__file__), "../messages"))
# sys.path.append(os.path.join(os.path.dirname(__file__)))
# from tornet_macOS.messages import error, log
from tornet_macOS.messages.error import error
from tornet_macOS.messages.log import log
from tornet_macOS.messages.print_banner import cyan

# from error import error
# from log import log

white = "\033[97m"
green = "\033[92m"
reset = "\033[0m"


def check_internet_connection():
    """First get URL from file Settings.txt for checking"""
    # settings_path = pkg_resources.resource_filename("tornet_macOS", "Settings.txt")
    InternetConnectionCheckURL = ""
    try:
        with importlib.resources.path("tornet_macOS", "Settings.txt") as settings_path:
            # print(settings_path)
            with open(settings_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("InternetConnectionCheckURL = "):
                        # Splitting by symbol "=" and removing space symbols and quotes symbols that we not need"
                        InternetConnectionCheckURL = (
                            line.split("=")[1].strip().strip('"').strip("'")
                        )
                        break
    except:
        settings_path = "tornet_macOS/"
        with open("tornet_macOS/Settings.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("InternetConnectionCheckURL = "):
                    # Разделяем по знаку = и убираем лишние пробелы и кавычки
                    InternetConnectionCheckURL = (
                        line.split("=")[1].strip().strip('"').strip("'")
                    )
                    break

    """
    with importlib.resources.path("tornet_macOS", "Settings.txt") as settings_path2:
        print(settings_path)
        with open(settings_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("InternetConnectionCheckURL = "):
                    # Splitting by symbol "=" and removing space symbols and quotes symbols that we not need"
                    InternetConnectionCheckURL = (
                        line.split("=")[1].strip().strip('"').strip("'")
                    )
                    break
    """

    """Check if internet connection is available"""
    log(
        f"checking internet connection by connecting to {cyan}"
        + InternetConnectionCheckURL
        + f"{reset}"
    )
    try:
        response = requests.get(InternetConnectionCheckURL, timeout=5)
        log("Available!")
        print(
            f'{green}    ( If you want to change check URL, please go to file: "{cyan}{settings_path}{green}" parameter: "{cyan}InternetConnectionCheckURL{green}" {reset})'
        )
        return True
    except requests.RequestException:
        error(
            f'Not available !!! If your provider blocking some Internet resourses you can change parameter "InternetConnectionCheckURL" in text file "{settings_path}" for URL that wasn\'t blocked. If not, check Your Internet connection',
            9,
        )
