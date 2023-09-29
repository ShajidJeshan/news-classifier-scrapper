import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com/style/look-of-the-week-kim-kardashian-buzz-cut/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extracting title
title = soup.find("h1").text

# Extracting all paragraphs
paragraphs = [p.text for p in soup.find_all("p")]

print("Title:", title)
print("Paragraphs:", paragraphs)
