<html>
<div align="center">

![TorNet Banner](https://img.shields.io/badge/TorNet_macOS-v1.0.0-008e50)
![Python](https://img.shields.io/badge/Python-3.11%2B-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-macOS_%20%7C%20Linux-222222)

</div>

# TorNet-macOS (for macOS and Linux)

TorNet-macOS is a Python package that automates IP address changes using Tor. It is a top tool for securing your networks by frequently changing your IP address, making it difficult for trackers to pinpoint your location.

TorNet-macOS is a fork of TorNet project for macOS users, but it also working on Linux too. It have some additionall API functions, that indicate not only your public IP, like in original version, but also indicates informton about country, country code, and city that was not accesible earlier. Also, now you can see time period before next IP changing by TorNet-macOS. DNS requests for API now is tor proxing by SOCKSv5!

<table>
  <tr align="center">
      <th style="width: 50%;">macOS</th>
      <th style="width: 50%;">Linux</th>
  </tr>
  <tr align="center">
      <td><img style="width: 100%; height: auto;" src="https://github.com/CoodeOSX/Filestorage/blob/main/img/macOS.png"/></td>
      <td><img style="width: 120%; height: auto;" src="https://github.com/CoodeOSX/Filestorage/blob/main/img/Linux.png"/></td>
  </tr>
</table>

Differences from [ayadseghairi](https://github.com/ayadseghairi/tornet) TorNet project:

- macOS supporting now! ))
- Indicate not only your public IP, but also informton about country, country code, and city.
- Indicate you time period before next IP changing by TorNet-macOS.
- Feature for deactivate showing IP or time period, or both by appending special commands.
- Feature, that let you change URL for checking your Internet connection. To make changes go to file: "tornet_macOS/Settings.txt" and change parameter: "InternetConnectionCheckURL".
- Now you can use you direct internet connection in parrallel with TorNet-macOS on your localhost, or you can link them by switching proxy in your OS settings. It's all will be ok wth your IP information detection.
- Fixed issue with exiting by pressing ctrl-C (now it stopping correctly with correct text message and exiting with correct code:0)
- Fixed issie with requests that sometimes doesen't show IP information by torsocks connection.
- DNS requests for API, when Tor connected, now is getting through Tor proxy only. It's preventing your DNS leackage now.
  * (But it's not prevent DNS requests leackage by your browser if you don't marked "Proxy DNS when using SOCKS v5" in your browser settings, so pay attention, and mark it, please!)

## Benefits

- **Enhanced Privacy**: By regularly changing your IP address, TorNet-macOS makes it much harder for websites and trackers to monitor your online activity.
- **Increased Security**: Frequent IP changes can help protect you from targeted attacks and make it more difficult for malicious actors to track your online presence.
- **Anonymity**: Using Tor, TorNet-macOS helps you maintain a high level of anonymity while browsing the internet.
- **Ease of Use**: TorNet-macOS is designed to be simple and easy to use, whether you prefer command-line tools or integrating it directly into your Python scripts.
- **Protection from Tracking**: With your IP address changing frequently, tracking services and advertisers will find it more challenging to build a profile on you.
- **Peace of Mind**: Knowing that your IP address is regularly changed can give you confidence in your online privacy and security.

## Check IP

```zsh
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip
```

## Check DNS Leak

https://dnsleaktest.com/

## Installation

### macOS:

require Python3 (Tested on 3.14.2) :

https://www.python.org/downloads/macos/

require Homebrew.So, if you didn't have, first install brew packet manager:

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
require Tor (Tor Expert Bundle). You can install it by running:

```zsh
brew install tor -y
```

Also you can install torsocks:

```zsh
brew install torsocks -y
```

To install TorNet-macOS, use pip3 (or pip, so change "pip3" to "pip" in command below):

```zsh
git clone https://github.com/CoodeOSX/tornet-macOS && mv tornet-macOS tornet_macOS && cd tornet_macOS && pip3 install .
```

### Linux:

To install TorNet-macOS, use pip:

```zsh
git clone https://github.com/CoodeOSX/tornet-macOS && mv tornet-macOS tornet_macOS && cd tornet_macOS && pip install .
```
If you have problems with packages, you may append "--break-system-packages" or use virtual environment

To install TorNet-macOS, use yay (Arch Linux):

```bash
yay -S git python && git clone https://github.com/CoodeOSX/tornet-macOS && mv tornet-macOS tornet_macOS && cd tornet_macOS && pip install .
```

## Usage

TorNet-macOS provides a command-line interface for easy use. Here are the available options:

```zsh
tornet_macOS --interval <seconds> --count <number>
```

- `--interval` (optional): Time in seconds between IP changes (default is 60 seconds).
- `--count` (optional): Number of times to change the IP (default is 10 times). If set to 0, the IP will be changed indefinitely.
- `--stop` (optional): Stop all Tor services and TorNet-macOS processes and exit.
- `--ip` (optional): Display the current IP address and exit.
- `--auto-fix` (optional): Automatically fix issues (install/upgrade packages).
- `--help`: Show the help message and exit.
- `--noip` (optional): Disable IP info monitoring.
- `--nosec` (optional): Disable waiting time monitoring.
- `--clear` (optional): clear screen before run.
- `--version`: Show the version number and exit.

## How It Works

TorNet-macOS uses the Tor network to route your internet traffic through multiple nodes, effectively masking your IP address. By periodically changing the IP address, TorNet-macOS ensures that your online activity remains anonymous and secure. This can be particularly useful for:

- **Privacy enthusiasts** who want to minimize their digital footprint.
- **Security professionals** who need to conduct penetration testing or other security assessments without revealing their true IP address.
- **Journalists and activists** operating in regions with internet censorship or surveillance.

### Examples

Change the IP address every 30 seconds, for a total of 5 times:

```bash
tornet_macOS --interval 30 --count 5
```

Change the IP address every 60 seconds indefinitely:

```bash
tornet_macOS --interval 60 --count 0
```

Stop all Tor services and TorNet-macOS processes:

```bash
tornet_macOS --stop
```

Display the current IP address:

```bash
tornet_macOS --ip
```

Automatically fix issues (install/upgrade packages):

```bash
tornet_macOS --auto-fix
```

## Configuring Your Browser to Use TorNet-macOS

To ensure your browser uses the Tor network for anonymity, you need to configure it to use TorNet-macOS's proxy settings:

1. **Firefox**: - Go to `Preferences` > `General` > `Network Settings`. - Select `Manual proxy configuration`. - Enter `127.0.0.1` for `SOCKS Host` and `9050` for the `Port` (or your specified values if different). - Ensure the checkbox `Proxy DNS when using SOCKS v5` is checked. - Click `OK`.

<img src="https://github.com/CoodeOSX/Filestorage/blob/main/img/socks5.png" alt="Firefox Configuration Example" />

## Troubleshooting

If you encounter any issues while using TorNet-macOS, here are a few steps you can take:

- Ensure that brew installed, if you are running macOS.
- Ensure that Tor is installed and running on your system.
- Make sure your internet connection is stable.
- Use the `--auto-fix` option to automatically install or upgrade required packages.
- Check the Tor logs for any error messages that might indicate connectivity problems.


## License

TorNet-macOS is released under the MIT License. See the LICENSE file for more details.

## Acknowledgements

We would like to thank the developers of the Tor project for their work in creating a robust and secure anonymity network.

## Thanks

Thank you for using TorNet-macOS! We hope this tool helps you secure your network and maintain your privacy. If you have any feedback or suggestions, please feel free to reach out to us.

Thanks for [ayadseghairi](https://github.com/ayadseghairi/tornet) that inspired me for creating this fork from his project.

Many thanks also to the original developer [ByteBreach](https://github.com/ByteBreach/tornet)
This project is an improvement to their own project

---

By following this guide, you should be able to effectively use TorNet-macOS to enhance your online privacy and security. Happy browsing!

<table>
  <tr align="center">
      <td><img style="width: 50%; height: auto;" src="https://github.com/CoodeOSX/Filestorage/blob/main/img/coconut.jpg"/><br /><sub><b>Coconut</b></sub></a></td>
      <td><img style="width: 30%; height: auto;" src="https://github.com/CoodeOSX/Filestorage/blob/main/img/penguin.png"/><br /><sub><b>Linux Penguin</b></sub></a></td>
  </tr>
</table>
</html>
