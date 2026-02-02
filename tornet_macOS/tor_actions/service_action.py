from tornet_macOS.checks.detect_service_manager import detect_service_manager
from tornet_macOS.messages.error import error
from tornet_macOS.messages.warning import warning
from tornet_macOS.run_cmd import run_cmd


def service_action(action):
    """Perform service action (start/stop/reload/restart) on tor"""
    service_mgr = detect_service_manager()
    if service_mgr == "systemctl":
        cmd = ["systemctl", action, "tor"]
        result = run_cmd(cmd, use_sudo=True, check=False)
        if result.returncode != 0:
            warning(f"Failed to {action} tor service: {result.stderr.strip()}")
    elif service_mgr == "service":
        cmd = ["service", "tor", action]
        result = run_cmd(cmd, use_sudo=True, check=False)
        if result.returncode != 0:
            warning(f"Failed to {action} tor service: {result.stderr.strip()}")
    elif service_mgr == "launchctl":
        cmd = ["brew", "services", action, "tor"]
        result = run_cmd(cmd, use_sudo=False, check=False)
        if result.returncode != 0:
            warning(f"Failed to {action} tor service: {result.stderr.strip()}")
    else:
        error(
            "No supported service manager found (systemctl or service or Homebrew)", 3
        )
