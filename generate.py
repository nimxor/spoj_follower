import re
import json
import codecs
import requests
import urllib
from bs4 import BeautifulSoup

url = 'http://www.spoj.com/users/rishiv30/'
html = urllib.urlopen(url).read()



soup = BeautifulSoup(html,"html.parser")

table = soup.find('table',attrs={'class':'table table-condensed'})

F = open('out.html','w')
ar=[]
for tr_tag in table.find_all('tr'):
	for a_tag in tr_tag.find_all('a'):
		P = str(a_tag.get_text()).strip()
		if P=="":
			continue
		problem_link = 'http://spoj.com'+a_tag['href']
		r = requests.get(problem_link)
		problem_status_html = r.text
		problem_status_html = problem_status_html.encode('ascii','ignore')
		problem_status_soup = BeautifulSoup(problem_status_html,"html.parser")
		Tab = problem_status_soup.find('table',attrs={'class':'problems table newstatus'})
		Tab = Tab.find('tbody')
		for row in Tab.find_all('tr'):
			entry = row.find('td',attrs={'class':'statusres'})
			STR = str(entry.get_text()).strip()
			if STR=="accepted":
				fin = str(row.find('td',attrs={'class':'status_sm'}).get_text()).strip()
				ar.append([fin,P])
				break

ar.sort()
