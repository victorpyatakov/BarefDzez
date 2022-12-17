import requests


class Tinkoff:

    @staticmethod
    def get_api_url(from_: str='RUB', to: str='AMD') -> str:
        return f"https://api.tinkoff.ru/v1/currency_rates?from={from_}&to={to}"

    @staticmethod
    def get_app_RUB_AMD(self) -> float:
        """ Exchange in APP """
        api_url = self.get_api_url()
        response =requests.get(api_url, verify=False)
        rates = response.json()['payload']['rates']
        app_RUB_AMD = rates[4]['buy']
        return app_RUB_AMD
    
    @staticmethod
    def get_cash_atm_RUB_AMD(self) -> float:
        """ Application payment and cash in ATM """
        api_url = self.get_api_url()
        response =requests.get(api_url, verify=False)
        rates = response.json()['payload']['rates']
        cash_atm_RUB_AMD = rates[10]['buy']
        return cash_atm_RUB_AMD

