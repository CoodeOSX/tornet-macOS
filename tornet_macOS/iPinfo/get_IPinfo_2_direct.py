from requests.sessions import Session

from tornet_macOS.messages.warning import warning


def get_IPinfo_2_direct():
    """Get IP address direct"""
    url = "https://ipapi.co/json/"
    s = Session()
    try:
        response = s.get(url, timeout=5)
        response.raise_for_status()
        # return response.text.strip()
        data = response.json()
        # print(data)
        return (
            "Direct",
            data.get("ip", "no ip"),
            data.get("country", "no country"),
            data.get("country_name", "no country name"),
            data.get("city", "no city"),
            "2",
            url,
        )
    except Exception as e:
        warning(
            f"API_2 Error: {e} Having trouble fetching IP address. Please, check your internet connection"
        )
        return None


# https://ipapi.co/12.255.255.255/json
