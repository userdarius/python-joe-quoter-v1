import requests

BARN_URL = "https://barn.traderjoexyz.com"
CHAIN = "avalanche"

AVAX_USDC_20BP = "0xD446eb1660F766d533BeCeEf890Df7A69d26f7d1"


def get(url: str, params=None):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Request failed")
    return response.json()


def get_bins(pair_address: str, id: int, radius: int):
    url = f"{BARN_URL}/v1/bin/{CHAIN}/{pair_address.lower()}/{id}"
    parameter = {"radius": radius}
    return get(url, parameter)


print(get_bins(AVAX_USDC_20BP, 8376042, 10))
