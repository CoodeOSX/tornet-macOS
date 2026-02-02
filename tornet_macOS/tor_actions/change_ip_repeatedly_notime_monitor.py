import time

from tornet_macOS.checks.what_OS import what_OS
from tornet_macOS.messages.error import error
from tornet_macOS.messages.print_IPinfo import print_IPinfo

from .change_ip_Darwin import change_ip_Darwin
from .change_ip_Linux import change_ip_Linux

# from .change_ip_Darwin import tordelay
from .parse_interval import parse_interval

# from .change_ip_Darwin import change_ip_Darwin
# from .change_ip_Linux import change_ip_Linux

cyan = "\033[36m"
tordelay = 3


def change_ip_repeatedly_notime_monitor(interval_str, count):
    """Change IP repeatedly with specified interval and count"""
    if what_OS() == "Darwin":
        if count == 0:  # Infinite loop
            while True:
                try:
                    sleep_time = parse_interval(interval_str)
                    if int(sleep_time or 0) < 3:
                        sleep_time = 3
                    else:
                        pass
                    time.sleep(int(sleep_time or 0) - tordelay)
                    # print(f"{cyan}reloading Tor...")
                    new_ip = change_ip_Darwin(tordelay)
                    # print(f"{cyan}reloaded!")
                    if new_ip:
                        # print("IP sucsessfully gotten")
                        print_IPinfo(new_ip)
                except KeyboardInterrupt:
                    break
        else:
            for _ in range(count):
                try:
                    sleep_time = parse_interval(interval_str)
                    if int(sleep_time or 0) < 3:
                        sleep_time = 3
                    else:
                        pass
                    time.sleep(int(sleep_time or 0) - tordelay)
                    # print(f"{cyan}reloading Tor...")
                    new_ip = change_ip_Darwin(tordelay)
                    # print(f"{cyan}reloaded!")
                    if new_ip:
                        # print("IP sucsessfully gotten")
                        print_IPinfo(new_ip)
                except KeyboardInterrupt:
                    break
    elif what_OS() == "Linux":
        if count == 0:  # Infinite loop
            while True:
                try:
                    sleep_time = parse_interval(interval_str)
                    if int(sleep_time or 0) < 3:
                        sleep_time = 3
                    else:
                        pass
                    time.sleep(int(sleep_time or 0) - tordelay)
                    # print(f"{cyan}reloading Tor...")
                    new_ip = change_ip_Linux(tordelay)
                    # print(f"{cyan}reloaded!")
                    if new_ip:
                        # print("IP sucsessfully gotten")
                        print_IPinfo(new_ip)
                except KeyboardInterrupt:
                    break
        else:
            for _ in range(count):
                try:
                    sleep_time = parse_interval(interval_str)
                    if int(sleep_time or 0) < 3:
                        sleep_time = 3
                    else:
                        pass
                    time.sleep(int(sleep_time or 0) - tordelay)
                    # print(f"{cyan}reloading Tor...")
                    new_ip = change_ip_Linux(tordelay)
                    # print(f"{cyan}reloaded!")
                    if new_ip:
                        # print("IP sucsessfully gotten")
                        print_IPinfo(new_ip)
                except KeyboardInterrupt:
                    break
    else:
        error("OS is unsupported:", 15)
