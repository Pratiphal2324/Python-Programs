import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/international/"
html = requests.get(url)
# print(html.text)
s = BeautifulSoup(html.text, "html.parser")
results = s.find_all("h3", class_="indicate-hover")
# articleTitle = results.find_all("h3", class_="indicate-hover css-si8ren")
for item in results:
    if item.a:
        print(item.a.text.replace("\n", " ").strip())
    else:
        print(item.contents[0].strip())
