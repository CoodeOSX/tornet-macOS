import random

from tornet_macOS.messages.error import error


def parse_interval(interval_str):
    """Parse interval string (single number or range)"""
    try:
        if "-" in str(interval_str):
            start, end = map(int, str(interval_str).split("-", 1))
            return random.randint(start, end)
        else:
            return int(interval_str)
    except ValueError:
        error(
            "Invalid interval format. Use number or range (e.g., '60' or '30-120', minimal value=3)",
            8,
        )
