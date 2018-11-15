import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'https://duelyst.gamepedia.com'
FILE_DIR = "resource/"

links = []
card_links = []
gifs =[]
download_links = []

def save_link(file_name, urls):
    with open(file_name, "w") as file:
        for url in urls:
            file.write(BASE_URL + ("%s\n"  % str(url)))

def load_link(file_name):
    urls = []
    with open(file_name, "r") as file:
        urls = file.read().split("\n")
    return urls

def download_file(url, name):
    with open(FILE_DIR + name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)

req = requests.get(BASE_URL + "/Duelyst_Wiki")
html = req.text
soup = BeautifulSoup(html, 'html.parser')

a_tags = soup.select(".fpsection2")[0].select('#fpsubject2')[2].find_all("a")
for i in range(0, len(a_tags), 2):
    links.append(a_tags[i]['href'])

save_link("urls01.txt", links)

for link in links:
    print(BASE_URL + link + " 방문")
    req = requests.get(BASE_URL + link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    tables = soup.select("tbody")
    for table in tables[1:]:
        for tr in table.find_all('tr')[1:]:
            try:
                card_links.append(tr.find_all('a')[0]['href'])
            except:
                pass
    
save_link("urls02.txt", card_links)

for link in card_links:
    print(BASE_URL + link + " 방문")
    req = requests.get(BASE_URL + link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all("a", "image")
    for image in images:
        href =image['href']
        if ".gif" in href:
            print(href + " 수집")
            gifs.append(href)

save_link("urls03.txt", gifs)

for link in gifs:
    req = requests.get(link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        d_link = soup.find_all("img", width=100)[0]["src"]

        print(d_link)
        download_links.append(d_link)
        download_file(d_link, link[35:])
    except:
        pass

save_link("download_links.txt", download_links)