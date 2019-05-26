# acknowledgements
# https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/beautiful_soup/beautiful_soup_and_requests.py
# https://github.com/llSourcell/web_scraper_live_demo/blob/master/main.py
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://stackoverflow.com/questions/5598524/can-i-remove-script-tags-with-beautifulsoup
# http://zetcode.com/python/beautifulsoup/

import requests
from bs4 import BeautifulSoup

result = requests.get("https://agentanakinai.wordpress.com/")

plain_text = result.text
soup = BeautifulSoup(plain_text,'lxml')
[s.extract() for s in soup(['iframe', 'script', 'style'])]
print(soup.get_text())
