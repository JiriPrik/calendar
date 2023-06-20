

class Pocasicitov:
    def __init__(self):
        self.st_place = ""
        self.st_temp_today = 0
        self.st_wind = 0
        self.st_data = []

    def data(self, url):
        from bs4 import BeautifulSoup
        import requests
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        # print(soup)
        thumbnail_elements = soup.find_all("div", class_="placemark")
        for element in thumbnail_elements:
            txt = element.text.replace(" ", "")
            txt = txt.strip("\n")
            self.st_place = txt

        thumbnail_elements = soup.find_all("span", id="wind-speed")
        for element in thumbnail_elements:
            txt = element.text.replace(" ", "")
            txt = txt.strip("\n")
            self.st_wind = txt + "km/h"

        thumbnail_elements = soup.find_all("div", class_="temp")
        for element in thumbnail_elements:
            txt = element.text.replace(" ", "")
            txt = txt.strip("\n")
            self.st_temp_today = txt

        thumbnail_elements = soup.find_all("img", class_="symbol")
        dt1 = []
        for element in thumbnail_elements:
            dt1.append(element['title'])
        self.st_data.append(dt1)

        dt2 = []
        thumbnail_elements = soup.find_all("div", class_="temperature max")
        for element in thumbnail_elements:
            el =element.text
            el = el.replace(" ", "")
            el = el.strip("\n")
            dt2.append(el)
        self.st_data.append(dt2)

        dt3 = []
        thumbnail_elements = soup.find_all("div", class_="temperature min")
        for element in thumbnail_elements:
            el = element.text
            el = el.replace(" ", "")
            el = el.strip("\n")
            dt3.append(el)
        self.st_data.append(dt3)