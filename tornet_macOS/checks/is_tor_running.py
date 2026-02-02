import os
import shutil
import subprocess


def is_tor_running():
    """Check if tor process is running"""
    if shutil.which("pgrep"):
        try:
            subprocess.run(["pgrep", "-x", "tor"], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            return False

    # Fallback: check /proc
    try:
        for pid in os.listdir("/proc"):
            if pid.isdigit():
                try:
                    with open(f"/proc/{pid}/comm", "r") as f:
                        if f.read().strip() == "tor":
                            return True
                except:
                    continue
    except:
        pass

    return False
