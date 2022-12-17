from .ineko import Ineko
from .sas import Sas
from .tinkoff import Tinkoff
import json

def get_current_exhange():
    result = {
        'INEKO': Ineko().get_RUB_AMD(),
        'SAS': Sas().get_RUB_AMD(),
        'TINKOFF_Cash': Tinkoff().get_cash_atm_RUB_AMD() ,
        'TINKOFF_APP_Exchange': Tinkoff().get_app_RUB_AMD(),
    }
    current_exhange = json.dumps(result, sort_keys=True, indent=4)
    return current_exhange