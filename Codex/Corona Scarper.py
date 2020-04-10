# If it doesn't work on pycharm or any other ide then try it on Google Colab
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total recovered: ", data[2].text.strip())
