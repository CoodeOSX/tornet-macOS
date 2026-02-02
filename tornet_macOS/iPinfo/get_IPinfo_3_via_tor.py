from requests.sessions import Session


# from tornet_macOS.messages.warning import warning
def get_IPinfo_3_via_tor():
    """Get IP address via Tor proxy"""
    url = "https://api.ipapi.is/"
    proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
    s = Session()
    s.trust_env = False  # Важно: отключаем системные настройки macOS
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
            data.get("location", {}).get("country_code", "no country_code"),
            data.get("location", {}).get("country", "no country name"),
            data.get("location", {}).get("city", "no city"),
            "3",
            url,
        )
    except Exception as e:
        """
        warning(
            f"API_3 Error: {e} Having trouble connecting to the Tor network. Please, wait a moment..."
        )
        """
        return None
