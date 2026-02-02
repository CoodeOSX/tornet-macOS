from requests.sessions import Session

from tornet_macOS.messages.warning import warning


def get_IPinfo_2_via_tor():
    """Get IP address via Tor proxy"""
    url = "https://ipapi.co/json/"
    proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
    s = Session()
    s.trust_env = False  # Important: disabling macOS System Preferences (Socks5h)
    s.proxies.update(proxies)
    try:
        response = s.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()
        # return response.text.strip()
        data = response.json()
        # print(data)
        return (
            "Tor",
            data.get("ip", "no ip"),
            data.get("country", "no country"),
            data.get("country_name", "no country name"),
            data.get("city", "no city"),
            "2",
            url,
        )
    except Exception as e:
        warning(
            f"API_2 Error: {e} Having trouble connecting to the Tor network or get IP info. Please, wait a moment..."
        )
        return None
