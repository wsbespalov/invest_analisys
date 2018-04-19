from lxml import html
import requests

class Invest(object):
    
    def __init__(self):
        self.URLS = {
            "eurusd": "https://m.investing.com/currencies/eur-usd"
        }
        self.xpaths = {
            "value": '//*[@id="siteWrapper"]/div[1]/section[2]/div[4]/div[2]/span[1]',
            "changes": '//*[@id="siteWrapper"]/div[1]/section[2]/div[4]/div[2]/span[2]/i[1]',
            "percent": '//*[@id="siteWrapper"]/div[1]/section[2]/div[4]/div[2]/span[2]/i[2]',
            "summary": '//*[@id="technicalInst"]/table[1]/tbody/tr[1]/td[2]/p',
            "ma": '//*[@id="technicalInst"]/table[1]/tbody/tr[2]/td[2]',
            "ti": '//*[@id="technicalInst"]/table[1]/tbody/tr[2]/td[2]',
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) \
            Gecko/20100101 Firefox/45.0'
        }
        self.__tree = None,
        self.__info = []
        self.__info_element = {
            "value": None,
            "changes": None,
            "percent": None,
            "summary": None,
            "ma": None,
            "ti": None,
            "technical": {
                "ma": {
                    "ma5": None,
                    "ma10": None,
                    "ma20": None,
                    "ma50": None,
                    "ma100": None,
                    "ma200": None,
                    "summary": None
                },
                "ti": {
                    "rsi": {
                        "value": None,
                        "action": None,
                    },
                    "stoch": {
                        "value": None,
                        "action": None,
                    },
                    "stochrsi": {
                        "value": None,
                        "action": None,
                    },
                    "macd": {
                        "value": None,
                        "action": None,
                    },
                    "atr": {
                        "value": None,
                        "action": None,
                    },
                    "adx": {
                        "value": None,
                        "action": None,
                    },
                    "cci": {
                        "value": None,
                        "action": None,
                    },
                    "highslows": {
                        "value": None,
                        "action": None,
                    },
                    "uo": {
                        "value": None,
                        "action": None,
                    },
                    "roc": {
                        "value": None,
                        "action": None,
                    },
                    "williams": {
                        "value": None,
                        "action": None,
                    },
                    "bullbear": {
                        "value": None,
                        "action": None,
                    }
                }
            }
        }

    def __get_html(self, url):
        page = requests.get(
            url=url,
            headers=self.headers
        )
        tree = html.fromstring(page.content)
        self.__tree = tree
        return tree

    def __get_value(self):
        value = self.__tree.xpath(self.xpaths["value"])
        self.__info_element["value"] = value[0].text.replace("\n", "").replace(" ", "")

    def __get_changes(self):
        value = self.__tree.xpath(self.xpaths["changes"])
        self.__info_element["changes"] = value[0].text.replace("\n", "").replace(" ", "")

    def __get_percent(self):
        value = self.__tree.xpath(self.xpaths["percent"])
        self.__info_element["percent"] = value[0].text.replace("\n", "").replace(" ", "")

    def __get_summary(self):
        value = self.__tree.xpath(self.xpaths["summary"])


    def scan_investing(self):
        self.__get_html(self.URLS["eurusd"])
        self.__get_value()
        self.__get_changes()
        self.__get_percent()

    def show_info(self):
        return self.__info

inv = Invest()
inv.scan_investing()
print(inv.show_info())
