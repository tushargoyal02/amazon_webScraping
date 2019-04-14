#!/usr/bin/python2

import cgi
import mysql.connector as mysql
from bs4 import BeautifulSoup
import requests
import time
import string

#connection between html page and python
print "Content-type: text/html\n\n"
data=cgi.FieldStorage()


print '''<br><br><br>
'''
img1=[None]*30
link=[None]*30
name=[None]*30
i=0
j=0
k=0

#extracting data from search portal
search=data.getvalue('search')

#CONCADINATING THE GIVEN VARIABLE WITH THE AMAZON SEARCH PAGE
url = ("http://www.amazon.in/s?keywords="+search)


req = requests.get(url).text

soup = BeautifulSoup(req,"lxml")


for img_div in soup.find_all("div",{"class":"s-item-container"}):
	for img_div2 in img_div.find_all("div",{"class":"a-fixed-left-grid"}):
		for img_div3 in img_div2.find_all("div",{"class":"a-fixed-left-grid-inner"}):
			for img_div4 in img_div3.find_all("div",{"class":"a-fixed-left-grid-col a-col-left"}):
				for img_div5 in img_div4.find_all("div",{"class":"a-row"}):
					for img_div6 in img_div5.find_all("div",{"class":"a-column a-span12 a-text-center"}):
						for img_id in img_div6.find_all("img",{"class":"s-access-image cfMarker"}):
							img1[i]=(img_id.get("src"))		
							i=i+1
							#GETTING ALL IMAGES LINKS IN (IMG1) VARIABLE	
							'''print "<br>"
							print "<td>"
							print '<img style="" src="'+img1+'"></td>'
							'''	

for name_div in soup.find_all("div",{"class":"s-item-container"}):
	for name_div2 in name_div.find_all("div",{"class":"a-fixed-left-grid"}):
		for name_div3 in name_div2.find_all("div",{"class":"a-fixed-left-grid-inner"}):
			for name_div4 in name_div3.find_all("div",{"class":"a-fixed-left-grid-col a-col-right"}):
				for name_div5 in name_div4.find_all("div",{"class":"a-row a-spacing-small"}):
					for name_div6 in name_div5.find_all("div",{"class":"a-row a-spacing-none"}):
						for name_a in name_div6.find_all("a",{"class":"a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"}):
							print ("d")
							name[i]=(name_a.get("title"))
							print name[i]	
							i=i+1
							
							


#APPLYING LOOP FOR SEARCHING DIV CLASS FOR THE (PRODUCT-ID)
for div in soup.find_all('div',{"class":"a-row a-spacing-none"}):
	#print div
	for a in div.find_all("a",{"class":"a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"}):	
		#print("helloooooo")		
		link[j]=(a.get('href'))
		j=j+1
		




count=0

print '<form action="http://192.168.43.40/cgi-bin/urltry.py" method="post">'
print '<input style=";" type="submit" value="Submit">'

while(count<=i):
	image= img1[count]
	link_url=link[count]
	abc=str(link_url)
	product_name=abc.split('/')[3]
	print '<table style="width:100%;"><tr><td><input type="radio" name="url" value="'+link_url+'"></td><td><img style="" src="'+image+'"></td><td>'+product_name+'</td><td>'+link_url+'</td></table>'
	count=count+1



print ('</form>')














