import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.globo.com/")

siteContent = BeautifulSoup(response.content, "html.parser")

firstNews = siteContent.find("div", attrs={"class": "wrapper"})

print("title: " + firstNews.find("h2", attrs={"class": "post__title"}).text)

print(
    "subtitle: "
    + firstNews.find("div", attrs={"class": "bullets"})
    .find("h2", attrs={"class": "post__title"})
    .text
)
