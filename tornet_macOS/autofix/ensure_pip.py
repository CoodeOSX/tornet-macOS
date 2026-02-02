import subprocess
import sys

from tornet_macOS.messages.error import error
from tornet_macOS.messages.log import log
from tornet_macOS.messages.warning import warning
from tornet_macOS.run_cmd import run_cmd

from .detect_package_manager import detect_package_manager
from .install_package import install_package
from .is_pip_installed import is_pip_installed


def ensure_pip():
    """Check pip installation"""
    if is_pip_installed():
        return True
    else:
        # warning("pip need to be Installed")
        """Ensure pip is available"""
        try:
            subprocess.run(
                [sys.executable, "-c", "import pip"], check=True, capture_output=True
            )
            return True
        except subprocess.CalledProcessError:
            log("attempting to install pip...")
            # Try ensurepip first
            cmd = [sys.executable, "-m", "ensurepip", "--upgrade"]
            try:
                run_cmd(
                    cmd,
                    use_sudo=False,
                    check=False,
                )
                print("upgrade")
                return True
            except:
                pass

            # Try system package manager
            try:
                pm = detect_package_manager()
                if pm == "apt":
                    install_package("python3-pip")
                elif pm in ["dnf", "yum"]:
                    install_package("python3-pip")
                elif pm == "pacman":
                    install_package("python-pip")
                elif pm == "apk":
                    install_package("py3-pip")
                elif pm == "zypper":
                    install_package("python3-pip")
                elif pm == "brew":
                    warning(
                        'Try: "python3 -m ensurepip --upgrade" in terminal manually if pip already is not installed yet, check it yourself! May be somethig going wrong if you see it'
                    )
                return True
            except:
                error("Failed to install pip. Please install pip manually.", 5)
