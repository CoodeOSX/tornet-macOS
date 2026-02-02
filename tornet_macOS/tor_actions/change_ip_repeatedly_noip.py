import time

from tornet_macOS.checks.what_OS import what_OS
from tornet_macOS.messages.error import error
from tornet_macOS.messages.log import log

from .parse_interval import parse_interval
from .service_action import service_action

cyan = "\033[36m"
tordelay = 3


def change_ip_repeatedly_noip(interval_str, count):
    """Change IP repeatedly with specified interval and count"""
    if what_OS() == "Darwin":
        if count == 0:  # Infinite loop
            while True:
                try:
                    sleep_time = parse_interval(interval_str)
                    log(f"{cyan}Waiting {sleep_time} sec..")
                    time.sleep(sleep_time or 30)
                    log(f"{cyan}reloading Tor...")
                    service_action("restart")
                    log(f"{cyan}reloaded!")
                except KeyboardInterrupt:
                    break
        else:
            for _ in range(count):
                try:
                    sleep_time = parse_interval(interval_str)
                    log(f"{cyan}Waiting {sleep_time} sec..")
                    time.sleep(sleep_time or 30)
                    log(f"{cyan}reloading Tor...")
                    service_action("restart")
                    log(f"{cyan}reloaded!")
                except KeyboardInterrupt:
                    break
    elif what_OS() == "Linux":
        if count == 0:  # Infinite loop
            while True:
                try:
                    sleep_time = parse_interval(interval_str)
                    log(f"{cyan}Waiting {sleep_time} sec..")
                    time.sleep(sleep_time or 30)
                    log(f"{cyan}reloading Tor...")
                    service_action("reload")
                    log(f"{cyan}reloaded!")
                except KeyboardInterrupt:
                    break
        else:
            for _ in range(count):
                try:
                    sleep_time = parse_interval(interval_str)
                    log(f"{cyan}Waiting {sleep_time} sec..")
                    time.sleep(sleep_time or 30)
                    log(f"{cyan}reloading Tor...")
                    service_action("reload")
                    log(f"{cyan}reloaded!")
                except KeyboardInterrupt:
                    break
    else:
        error("OS is unsupported:", 13)
