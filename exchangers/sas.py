import requests
from bs4 import BeautifulSoup

class Sas:


    def get_api_url(self) -> str:
        return 'https://www.sas.am/en/appfood/personal/calculator/'


    def get_RUB_AMD(self) -> float:
        url = self.get_api_url()
        soup = BeautifulSoup(requests.get(url).content)
        exc_tab = soup.find_all("div", {"class": "exchange-table"})
        exce_tab_row = exc_tab[0].find_all("div", {"class": "exchange-table__row"})
        exc_tab_cell_content= exce_tab_row[3].find_all("span", 
                                                       {
                                                        "class": "exchange-table__cell-content"
                                                       })
        RUB_AMD = float(exc_tab_cell_content[1].text)
        return RUB_AMD