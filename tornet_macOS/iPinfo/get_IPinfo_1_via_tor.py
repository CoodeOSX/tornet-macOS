from requests.sessions import Session


# from tornet_macOS.messages.warning import warning
def get_IPinfo_1_via_tor():
    """Get IP address via Tor proxy"""
    url = "http://ip-api.com/json/"
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
            data.get("query", "no ip"),
            data.get("countryCode", "no countryCode"),
            data.get("country", "no country name"),
            data.get("city", "no city"),
            "1",
            url,
        )
    except Exception as e:
        """
        warning(
            f"API_1 Error: {e} Having trouble connecting to the Tor network. Please, wait a moment..."
        )
        """
        return None
