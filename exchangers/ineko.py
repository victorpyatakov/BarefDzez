import requests
import json

class Ineko:


    def get_api_url(self) -> str:
        return "https://www.inecobank.am/api/rates/"


    def get_RUB_AMD(self) -> float:
        """ RUB to DRAM in APP """
        api_url = self.get_api_url()
        response = requests.get(api_url, verify=False)
        items = response.json()['items']
        RUB_AMD = items[2]['online']['buy']
        return RUB_AMD


if __name__ == "__main__":
    api_url = Ineko.get_api_url()
    response = requests.get(api_url, verify=False)
    d = json.dumps(response.json(), sort_keys=True, indent=4)
    print(d)