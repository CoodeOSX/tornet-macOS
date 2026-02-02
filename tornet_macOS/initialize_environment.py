from tornet_macOS.messages.log import log
from tornet_macOS.tor_actions.service_action import service_action


def initialize_environment():
    """Initialize tor environment"""
    service_action("start")
    log("Tor service started. Please wait for Tor to establish connection.")
    log("Configure your browser to use Tor proxy (127.0.0.1:9050) for anonymity.")
