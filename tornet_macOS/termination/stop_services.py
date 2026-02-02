# import subprocess

from tornet_macOS.messages.log import log
from tornet_macOS.messages.print_banner import TOOL_NAME
from tornet_macOS.tor_actions.service_action import service_action


def stop_services():
    """Stop tor service and tornet processes"""
    service_action("stop")
    """
    try:
        subprocess.run(["pkill", "-f", TOOL_NAME], check=False, capture_output=True)
    except:
        pass
    """
    log(f"Tor services and processes stopped. Exiting {TOOL_NAME}...")
