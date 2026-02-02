import argparse
import signal
import time

from tornet_macOS.autofix.auto_fix import auto_fix
from tornet_macOS.checks.check_internet_connection import check_internet_connection
from tornet_macOS.checks.is_tor_installed import is_tor_installed
from tornet_macOS.clear_terminalscreen import clear_terminalscreen
from tornet_macOS.initialize_environment import initialize_environment
from tornet_macOS.iPinfo.get_current_IPinfo import get_current_IPinfo
from tornet_macOS.messages.error import error
from tornet_macOS.messages.print_banner import VERSION, print_banner
from tornet_macOS.messages.print_IPinfo import print_IPinfo
from tornet_macOS.termination.signal_handler import signal_handler
from tornet_macOS.termination.stop_services import stop_services
from tornet_macOS.tor_actions.change_ip_repeatedly import change_ip_repeatedly
from tornet_macOS.tor_actions.change_ip_repeatedly_noip import change_ip_repeatedly_noip
from tornet_macOS.tor_actions.change_ip_repeatedly_noip_nosec import (
    change_ip_repeatedly_noip_nosec,
)
from tornet_macOS.tor_actions.change_ip_repeatedly_notime_monitor import (
    change_ip_repeatedly_notime_monitor,
)


def main():
    """Main function"""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)

    parser = argparse.ArgumentParser(
        description="TorNet - Automate IP address changes using Tor"
    )
    parser.add_argument(
        "--interval",
        type=str,
        default="60",
        help='Time in seconds between IP changes (or range like "30-120") Minimal value 3',
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of times to change IP. If 0, change IP indefinitely",
    )
    parser.add_argument(
        "--ip", action="store_true", help="Display current IP address and exit"
    )
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Automatically install missing dependencies",
    )
    parser.add_argument(
        "--stop", action="store_true", help="Stop all Tor services and tornet processes"
    )
    parser.add_argument(
        "--noip",
        action="store_true",
        help="Disable IP info monitoring",
    )
    parser.add_argument(
        "--nosec",
        action="store_true",
        help="Disable waiting time monitoring",
    )
    parser.add_argument("--clear", action="store_true", help="clear screen before run")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

    args = parser.parse_args()
    if args.clear:
        clear_terminalscreen()
        pass

    if args.stop:
        stop_services()
        return

    if args.ip:
        ip = get_current_IPinfo()
        if ip:
            print_IPinfo(ip)
        return

    if args.noip and args.nosec:
        print_banner()
        check_internet_connection()
        initialize_environment()
        change_ip_repeatedly_noip_nosec(args.interval, args.count)
        return

    if args.noip:
        print_banner()
        check_internet_connection()
        initialize_environment()
        change_ip_repeatedly_noip(args.interval, args.count)
        return

    if args.nosec:
        print_banner()
        check_internet_connection()
        initialize_environment()
        # Wait for tor to establish connection
        time.sleep(5)
        print_IPinfo(get_current_IPinfo())
        change_ip_repeatedly_notime_monitor(args.interval, args.count)
        return

    if args.auto_fix:
        auto_fix()
        return

    # Check dependencies
    if not is_tor_installed():
        error("Tor is not installed. Run with --auto-fix to install automatically.", 10)

    try:
        import requests
    except ImportError:
        error(
            "requests package not found. Run with --auto-fix to install automatically.",
            11,
        )

    print_banner()
    check_internet_connection()
    initialize_environment()

    # Wait for tor to establish connection
    time.sleep(5)
    print_IPinfo(get_current_IPinfo())
    change_ip_repeatedly(args.interval, args.count)


# tornet()
if __name__ == "__main__":
    main()
