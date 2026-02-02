from requests.sessions import Session


# from tornet_macOS.messages.warning import warning
def get_IPinfo_3_direct():
    """Get IP address direct"""
    url = "https://api.ipapi.is/"
    s = Session()
    s.trust_env = False  # Important: disabling macOS System Preferences (Socks5h)
    try:
        response = s.get(url, timeout=5)
        response.raise_for_status()
        # return response.text.strip()
        data = response.json()
        # print(data)
        return (
            "Direct",
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
