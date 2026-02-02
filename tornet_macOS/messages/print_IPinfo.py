from .log import log

green = "\033[92m"
white = "\033[97m"
# blue = "\033[34m"


def print_IPinfo(APIinfo):
    """Print current IP info"""
    if APIinfo != None:
        log(
            f"Your {APIinfo[0]} IP address is: {white}{APIinfo[1]}{green} Country: {white}{APIinfo[2]} ({APIinfo[3]}){green},{white}{APIinfo[4]}"
        )
    else:
        pass


"""
log(
    f"Your {APIinfo[0]} IP address is: {white}{APIinfo[1]}{green} Country: {white}{APIinfo[2]} ({APIinfo[3]}){green},{white}{APIinfo[4]}{blue}, {APIinfo[5]}, {APIinfo[6]}"
)
"""
