from requests import get
from datetime import datetime


# API KEY created in etherscan.io
API_KEY = '62XA11P6M2XFIXWD9SKARQTMFQMKY8FP6K'
BASE_URl = "https://api.etherscan.io/api"
yy = mm = dd = h = min = seg = 0
date4 = [yy, mm, dd, h, min, seg]
ETHER_VALUE = 10 ** 18
blockchain_error = blockchain_min_value_tx = []
blockchain_out_of_gas_tx = blockchain_execution_reverted_tx = []
i = 0
initial_time_estimated = 0


# Side Defs
def make_api_url(module, action, **kwargs):
    """Returns url"""
    url = BASE_URl + f'?module={module}&action={action}&apikey={API_KEY}'
    for k, v in kwargs.items():
        url += f'&{k}={v}'
    return url


def get_block_byTimeStamp(get_timestamp):
    """Returns the API response"""
    call_block_no = get(make_api_url(
        "block", "getblocknobytime",
        timestamp=get_timestamp, closest="before")).json()
    return call_block_no["result"]


def get_block_by_date(input_data):
    """Return block by a specific date"""
    date = input_data.split()  # Ex: ["2023","4","17"]
    date_in_datetime = datetime(*map(int, date))
    timeStamp = datetime.timestamp(date_in_datetime).__trunc__()
    block = get_block_byTimeStamp(timeStamp)
    return block


def last_block():
    """Get last block in ethereum mainnet"""
    BLOCK_NUMBER = get(make_api_url("proxy", "eth_blockNumber")).json()
    return int(BLOCK_NUMBER["result"], base=16)


def get_block_numbers():
    """Get Blocks number by date"""
    start_block_date = get_block_by_date(input("Start date:"))
    end_block_date = get_block_by_date(input("End date: "))
    return start_block_date, end_block_date


data = get(make_api_url(module="account", action="balance",
                        address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", tag="latest"))


print(data.json())
