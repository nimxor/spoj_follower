import re
import json
import codecs
import requests
import urllib
from bs4 import BeautifulSoup

fhand = codecs.open('where.js','w', "utf-8")
fhand.write("[\n")

def gettitle(st):
	t=st.find(':')
	return st[3:t-1]

url ="https://discuss.codechef.com/questions/48877/data-structures-and-algorithms"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")

tags = soup.find('div', attrs={'class':"question-body"})

count = 0

for ptag in tags.find_all('p'):
	title = gettitle(str(ptag))
	count = count + 1
        if count > 1 : 
        	fhand.write(",\n")
	output = "[\n{'title':'"+title+"'},"
	for atag in ptag.find_all('a'):
		output += "\n{'"+atag.contents[0]+"':'"+atag.get('href',None)+"'},"
	output = output[:-1]+'\n]'
	fhand.write(output)

fhand.write("\n];\n")
fhand.close()