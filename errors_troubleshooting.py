modules_call_error = {
    "!!Deprecated!! error 2": [
        "tornet_macOS.run_cmd",
        "Root privileges required but sudo not available. Run as root or install sudo.",
    ],
    "error 3": [
        "tornet_macOS.tor_actions.service_action",
        "No supported service manager found (systemctl or service or Homebrew)",
    ],
    "error 4": [
        "tornet_macOS.autofix.install_package",
        "No supported package manager found. Please install packages manually.",
    ],
    "error 5": [
        "tornet_macOS.autofix.ensure_pip",
        "Failed to install pip. Please install pip manually.",
    ],
    "error 6": [
        "tornet_macOS.autofix.ensure_requests",
        "Failed to install requests package.",
    ],
    "error 7": [
        "tornet_macOS.autofix.ensure_tor",
        "Failed to install tor. Please install tor manually.",
    ],
    "error 8": [
        "tornet_macOS.tor_actions.parse_interval",
        "Invalid interval format. Use number or range (e.g., '60' or '30-120', minimal value=3)",
    ],
    "error 9": [
        "tornet_macOS.checks.check_internet_connection",
        'Not available !!! If your provider blocking some Internet resourses you can change parameter "InternetConnectionCheckURL" in text file "{settings_path}" for URL that wasn\'t blocked. If not, check Your Internet connection',
    ],
    "error 10": [
        "main",
        "Tor is not installed. Run with --auto-fix to install automatically.",
    ],
    "error 11": [
        "main",
        "requests package not found. Run with --auto-fix to install automatically.",
    ],
    "error 12": ["tornet_macOS.tor_actions.change_ip_repeatedly", "OS is unsupported:"],
    "error 13": [
        "tornet_macOS.tor_actions.change_ip_repeatedly_noip",
        "OS is unsupported:",
    ],
    "error 14": [
        "tornet_macOS.tor_actions.change_ip_repeatedly_noip_nosec",
        "OS is unsupported:",
    ],
    "error 15": [
        "tornet_macOS.tor_actions.change_ip_repeatedly_notime_monitor",
        "OS is unsupported:",
    ],
    "error Variable2": [
        "tornet_macOS.messages.what_OS",
        "Unknown OS detecting error : unsupported OS {e}",
    ],
    "error Variable3_See_error 2": [
        "tornet_macOS.run_cmd",
        "Command failed: {' '.join(cmd)}\nerror : {e.stderr.strip()}",
    ],
}
