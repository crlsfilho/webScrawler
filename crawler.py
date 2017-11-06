from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.muitomaisdigital.com.br'

uCLient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

container = page_soup.findAll("div", {"class":"item-container"}
