import requests
from bs4 import BeautifulSoup

tincof_rub_usd = 70
# tincof_rub_dram = 5,64
tincof_rub_dram_perevod = 5.86

# tincof
#https://api.tinkoff.ru/v1/currency_rates?from=RUB&to=AMD
# "category": "DebitCardsTransfers"
# "category": "DepositPayments",

sas_rub_dram = 6.15

# ineko
# https://www.inecobank.am/api/rates/

ineco_online_rub_dram = 6.13

def get_cur_rate():
    return {   

        "tincof": tincof_rub_dram_perevod,
        "sas": sas_rub_dram,
        "ineco_online": ineco_online_rub_dram
    }

def rub_to_dram(rub_count):
    result = {
        "rub": rub_count,
        "tincof": rub_count * tincof_rub_dram_perevod,
        "sas": rub_count * sas_rub_dram,
        "ineco_online": rub_count * ineco_online_rub_dram
    }
    return result

print(rub_to_dram(1000))

# TODO

# rub -> amd

def get_ineco_online():
    tin =requests.get("https://www.inecobank.am/api/rates/",verify=False)
    items = tin.json()['items']
    return {'RUB to DRAM in APP':items[2]['online']['buy']} # рубли в драмы в прилке

def get_tin_exchange():
    tin =requests.get("https://api.tinkoff.ru/v1/currency_rates?from=RUB&to=AMD",verify=False)
    rates = tin.json()['payload']['rates']
    return {'Exchange in APP': rates[4]['buy'], 
            'Application payment and cash in ATM': rates[10]['buy']} # курс в прило
   
def get_sas_exchange():
    soup = BeautifulSoup(requests.get('https://www.sas.am/en/appfood/personal/calculator/').content)
    divTag = soup.find_all("div", {"class": "exchange-table"})
    a = divTag[0].find_all("div", {"class": "exchange-table__row"})
    c = a[3].find_all("span", {"class": "exchange-table__cell-content"})
    return {'SAS RUB to DRAM': float(c[1].text)}


if __name__ == "__main__":
    import json

    d = {
        'ineco': get_ineco_online(),
        'sas':get_sas_exchange(),
        'tincoff':get_tin_exchange()
    }
    d = json.dumps(d, sort_keys=True, indent=4)
    print(d)
    
    
    







