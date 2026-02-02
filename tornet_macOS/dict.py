def get_IPinfo_Dict():
    """It's module for testing logic for API, without using API"""
    w = 5
    if w > 0:
        mydict = {
            "ip": "185.241.208.96",
            "network": "185.241.208.0/24",
            "version": "IPv4",
            "city": "Warsaw",
            "region": "Mazovia",
            "region_code": "14",
            "country": "PL",
            "country_name": "Poland",
            "country_code": "PL",
            "country_code_iso3": "POL",
            "country_capital": "Warsaw",
            "country_tld": ".pl",
            "continent_code": "EU",
            "in_eu": True,
            "postal": "00-002",
            "latitude": 52.2372,
            "longitude": 21.0123,
            "timezone": "Europe/Warsaw",
            "utc_offset": "+0100",
            "country_calling_code": "+48",
            "currency": "PLN",
            "currency_name": "Zloty",
            "languages": "pl",
            "country_area": 312685.0,
            "country_population": 37978548,
            "asn": "AS210558",
            "org": "1337 Services GmbH",
        }

        value1 = mydict.get("ip")
        value2 = mydict.get("country")
        value3 = mydict.get("country_name")
        value4 = mydict.get("city")

        return ("Dict", value1, value2, value3, value4, 4, "www.bubbles.net")
    else:
        return None


# print(get_info()[3])
