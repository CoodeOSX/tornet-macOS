from tornet_macOS.checks.is_tor_running import is_tor_running

from .get_IPinfo_2_direct import get_IPinfo_2_direct
from .get_IPinfo_2_via_tor import get_IPinfo_2_via_tor
from .get_IPinfo_3_direct import get_IPinfo_3_direct
from .get_IPinfo_3_via_tor import get_IPinfo_3_via_tor


def get_current_IPinfo():
    """Get current public IP address"""
    if is_tor_running():
        if get_IPinfo_3_via_tor() != None:
            return get_IPinfo_3_via_tor()
        else:
            return get_IPinfo_2_via_tor()
    else:
        if get_IPinfo_3_direct != None:
            return get_IPinfo_3_direct()
        else:
            return get_IPinfo_2_direct()
