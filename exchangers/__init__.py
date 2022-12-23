from .ineko import Ineko
from .sas import Sas
from .tinkoff import Tinkoff
import json

def get_current_exhange():
    result = {
        'INEKO': Ineko().get_RUB_AMD(),
        'SAS': Sas().get_RUB_AMD(),
        'TINKOFF_MIR': Tinkoff().get_cash_atm_RUB_AMD() ,
        'TINKOFF_APP_Exchange': Tinkoff().get_app_RUB_AMD(),
    }
    current_exhange = json.dumps(result, sort_keys=True, indent=4)
    return current_exhange


def get_amd_rub(amd):
    result = {
        'INEKO': round(amd / Ineko().get_RUB_AMD(), 2),
        'SAS': round(amd / Sas().get_RUB_AMD(), 2),
        'TINKOFF_MIR': round(amd / Tinkoff().get_cash_atm_RUB_AMD(), 2) ,
        'TINKOFF_APP_Exchange': round(amd / Tinkoff().get_app_RUB_AMD(), 2),
    }
    current_exhange = json.dumps(result, sort_keys=True, indent=4)
    return current_exhange