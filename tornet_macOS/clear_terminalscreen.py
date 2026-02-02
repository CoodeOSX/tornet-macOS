import subprocess

from tornet_macOS.checks.what_OS import what_OS


def clear_terminalscreen():
    if what_OS() == "Linux":
        subprocess.run("clear")
    elif what_OS() == "Darwin":
        subprocess.call('clear && printf "\033[3J"', shell=True)
    else:
        pass
