dblack = "\033[30m"
black = "\033[90m"
dgreen = "\033[32m"
green = "\033[92m"
yellow = "\033[33m"
byellow = "\033[93m"
magenta = "\033[35m"
bmagenta = "\033[95m"
dred = "\033[31m"
red = "\033[91m"
white = "\033[97m"
bblue = "\033[94m"
blue = "\033[34m"
dwhite = "\033[37m"
reset = "\033[0m"
cyan = "\033[36m"
bcyan = "\033[96m"
background = cyan
picture = dwhite
nose = byellow
TOOL_NAME = "TorNet-macOS"
VERSION = "1.0.0"


def print_banner():
    banner = f"""{background}
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░{white} {TOOL_NAME} {background}░░░░░░░░{picture}--{background}░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░{picture}*+{background}░░░░░░░░░░░{black} & {background}░░░░░░░░{picture} %▒▒▒▒▒▒▒▒% {background}░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░{picture}-{background}░░░░░░░░░░░░{red}Linux{background}░░░░░░{picture}.%%%%%%%%%%%%.{background}░░░░░░░░░░
    ░░░░░░░░{picture}%::*%#%%--***+*▒@{background}░░░░░░   ░░░░░░{picture} +=███▓***:.=*+ {background}░░░░░░░░░
    ░░░░░░{picture}+*%%@@%▓█@▒@▒▓█▓-*%▒@{background}░░░░░░░░░░░░{picture}   ▒▒.▒ %:▒▒▒▓▒   {background}░░░░░░░░
    ░░░░{picture}▒-%#@@%%%%%▒@@@@@█▓-==+▒{background}░░░░░░░░░░░{picture}   ▓▒;▒ + ▒.▒▒▒   {background}░░░░░░░░
    ░░░{picture}▓=%@▒%%%%#%%##%%%%▓▒=*=**@{background}░░░░░░░░░{picture}     @{nose}▓***@▓█{picture}*{picture}      {background}░░░░░░░
    ░░░{picture}+*#@%%%%%###%###%@██=-=-+#{background}░░░░░░░░{picture}     ██{nose}▓%****▒{picture}███     {background}░░░░░░
    ░░░{picture}#@▓█%%%######*%#%█▓::#-**={background}░░░░░░{picture}-:   █▓▓▓▓▓{nose}▒%%{picture}▓▓▓▓▓▓▓   :- {background}░░░
    ░░░░{picture}=@▒▒%%#%####%██▓▒#-.-+=**{background}░░░░{picture}*      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     *{background}░░
    ░░░░{picture}*:%@▓▒%#%%%█▓-.::-: =++%{background}░░░░{picture}  {background}░░░{picture}  ▒@@@@@@@@@@@@@@@@▒  {background}░░░{picture}  {background}░
    ░░░░░{picture}%=▓▒▒▓▓▓██=-.#-=+-===+@{background}░░░░░░░░░{picture}  ▒@@@@@@@@@@@@@@@@▒  {background}░░░░░░
    ░░░░░░{picture}@%.:%@▓▓:.-:=-+-.--*{background}░░░░░░░░░░░░{picture} #@@@@@@@@@@@@@@@@▒.{background}░░░░░░░
    ░░░░░░░░░{picture}+-:-.=..:.-::-+▓{background}░░░░░░░░░░░░░{picture}*▒{nose}▓▓%**%{picture}@@@@{nose}%**#▓{picture}▓▒#{background}░░░░░░░
    ░░░░░░░░░░{picture}%+-:......:=*@{background}░░░░░░░░░░░░{picture}*{nose}%%%%%%%***{picture}%%{nose}***%%%%%%%{picture}*{background}░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{picture}{nose}***********{picture}**{nose}***********{background}░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    {byellow}                          Version: {VERSION}
    {white}+--------------------------{cyan}({red}ByteBreach{cyan}){white}-------------------------+{reset}
    {white}+-------------------{cyan}({red}Improved by Ayad Seghiri{cyan}){white}------------------+{reset}
    {white}+---------{cyan}({red}Adaptation for macOS and {cyan}IP info {red}by {white}CoodeOSX{cyan}){white}--------+{reset}
    """
    print(banner)
