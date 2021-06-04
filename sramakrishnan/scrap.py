import requests
from bs4 import BeautifulSoup

def ExtractData(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    head = (soup.head).text.strip()
    body = (soup.body).text.strip()
    f = open("demo.txt", "a")
    f.write(head)
    f.write(body)
    f.close()
    

ExtractData(url="https://www.sramakrishnan.com/")