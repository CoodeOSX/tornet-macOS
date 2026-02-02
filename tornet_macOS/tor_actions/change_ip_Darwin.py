import time

from tornet_macOS.iPinfo.get_current_IPinfo import get_current_IPinfo

from .service_action import service_action


def change_ip_Darwin(tordelay):
    """Change IP by reloading Tor service"""
    service_action("restart")
    time.sleep(tordelay)  # Wait for new circuit
    return get_current_IPinfo()
