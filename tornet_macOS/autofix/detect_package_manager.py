import shutil


def detect_package_manager():
    """Detect available package manager"""
    managers = [
        ("apt", ["apt-get"]),
        ("dnf", ["dnf"]),
        ("yum", ["yum"]),
        ("pacman", ["pacman"]),
        ("apk", ["apk"]),
        ("zypper", ["zypper"]),
        ("brew", ["brew"]),
    ]

    for pm, binaries in managers:
        if any(shutil.which(binary) for binary in binaries):
            return pm
    return None
