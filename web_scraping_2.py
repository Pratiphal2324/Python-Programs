import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
html = requests.get(url)
s = BeautifulSoup(html.text, "html.parser")
results = s.find_all(class_="body__inner-container")
# print(results)
r = ""
for item in results:
    r = r + item.get_text()
print(r)
