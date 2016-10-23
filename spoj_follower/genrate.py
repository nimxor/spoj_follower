import re
import json
import codecs
import requests
import urllib
from bs4 import BeautifulSoup

url ="http://www.spoj.com/users/shubham190496/"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")

tags = soup.find('div', attrs={'id':"user-profile-tables"})

l=[]

for ptag in tags.find_all('a'):
	st = "http://www.spoj.com" + str(ptag['href'])
	html = urllib.urlopen(st).read()
	soup = BeautifulSoup(html,"html.parser")
	tagg = soup.find('tr', attrs={'class':"kol1"})
	ttd = tagg.find_all('td')
	time =  str(ttd[1].find('span').contents)
	problem_name = ttd[2].find('a')
	problem_title= str(problem_name['title'])
	# print(problem_name)
	problem_link = problem_name['href']
	s = "http://www.spoj.com" + str(problem_link)
	ss = time[3:-2]
	p = ss.split(' ')
	print ss
	# print([p[0],p[1],problem_title,s])
	# print problem_title + "->" + s
	# l.append([p[0],p[1],problem_title,s])
	# print 
	# print he
		# text = ttd.text.replace('&nbsp;', '').lstrip()
  #       print text



	# st = http://www.spoj.com/status/CASHIER,xilinx/

# for link in l:
# 	print link