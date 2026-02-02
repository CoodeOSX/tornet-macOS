import shutil
import os

def detect_service_manager():
    """Detect if systemd or sysv init is used"""
    if shutil.which("systemctl") and os.path.exists("/run/systemd/system"):
        return "systemctl"
    elif shutil.which("service"):
        return "service"
    elif shutil.which("launchctl") and os.path.exists("/bin/launchctl"):
        return "launchctl"
    return None
