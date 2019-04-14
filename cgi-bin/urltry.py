#!/usr/bin/python2

import cgi
import requests
from bs4 import BeautifulSoup
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from textblob import TextBlob
import string
import mpld3
import sys
import webbrowser


reload(sys)
sys.setdefaultencoding('utf-8')


#connection between html page and python
print ("Content-type: text/html\n\n")
data=cgi.FieldStorage()

url=data.getvalue('url')

#url="https://www.amazon.in/dp/B071HWTHPH/ref=dp_cerb_1"
data=requests.get(url).content

soup = BeautifulSoup(data,"lxml")
#soup1 = BeautifulSoup(data,"lxml")
for div in soup.find_all("div",{"id":"titleSection"},{"class":"a-section a-spacing-none"}):
	#print('oooooo')
	for h1 in div.find_all("h1",{"id":"title"},{"class":"a-size-large a-spacing-none"}):
		#print(h1)
		for span in h1.find_all("span",{"id":"productTitle"},{"class":"a-size-large"}):
			span1=span.text
			
#print("hello1")



#FOR IMAGE link Extraction 

for img_div in soup.find_all("div",{"id":"imgTagWrapperId"},{"class":"imgTagWrapper"}):
	#print("okkkkk")
	for img_id in img_div.find_all("img",{"id":"landingImage"},{"class":"a-dynamic-image a-stretch-vertical"}):
		img1=(img_id.get('src'))
		#GETTING ALL IMAGES LINKS IN (IMG1) VARIABLE		
		#print(img1)			
			
#print("hello2")
#FOR PRICE 
for pri_div in soup.find_all("div",{"id":"price"},{"class":"a-section a-spacing-small"}):
	#print("lalala")
	for pri_table in pri_div.find_all("table",{"class":"a-lineitem"}):
		#print("okkk")	
			for pri_span in pri_table.find_all("span",{"id":"priceblock_ourprice"},{"class":"a-size-medium a-color-price"}):
			#for pri_span2 in pri_span.find_all("span",{"class":"currencyINR"}):
				price=(pri_span.text)	
				#print(price)
				k1=price.encode("utf-8")
				#print(k1)

#print("hello3")

x1=0
x2=0
x3=0
x4=0
x5=0
#for Stars
for star_div in soup.findAll("div",{"class":"a-row"}):
	for star_i in star_div.findAll("i",{"class":"a-icon a-icon-star a-star-1 review-rating"},{"data-hook":"review-star-rating-view-point"}):
		for star_span in star_i.findAll('span',{"class":"a-icon-alt"}):
			x1 = x1+1

	for star_i in star_div.findAll("i",{"class":"a-icon a-icon-star a-star-2 review-rating"},{"data-hook":"review-star-rating-view-point"}):
		for star_span in star_i.findAll('span',{"class":"a-icon-alt"}):
			x2 = x2+1

	for star_i in star_div.findAll("i",{"class":"a-icon a-icon-star a-star-3 review-rating"},{"data-hook":"review-star-rating-view-point"}):
		for star_span in star_i.findAll('span',{"class":"a-icon-alt"}):
			x3 = x3+1

	for star_i in star_div.findAll("i",{"class":"a-icon a-icon-star a-star-4 review-rating"},{"data-hook":"review-star-rating-view-point"}):
		for star_span in star_i.findAll('span',{"class":"a-icon-alt"}):
			x4 = x4+1

	for star_i in star_div.findAll("i",{"class":"a-icon a-icon-star a-star-5 review-rating"},{"data-hook":"review-star-rating-view-point"}):
		for star_span in star_i.findAll('span',{"class":"a-icon-alt"}):
			x5 = x5+1	



#print("hello4")		



# [ FOR REVIEWS ] 

positive  = 0
negative = 0
neutral = 0
polarity = 0
i=1
print('\n\n')
#for rev_div in soup.find_all("div",{"class":"a-row a-spacing-medium review-data"}):
#	for rev_span in rev_div.find_all("span",{"class":"a-size-base review-text"},{"data-hook":"review-body"}):
#---------------------------------------------------------------------------------------------------------------------
# new implemented


for rev_div in soup.find_all("div",{"class":"a-row a-spacing-small review-data"}):
        #print("hey")
	#print("hello",rev_div)
        for rev_span in rev_div.find_all("span",{"class":"a-size-base review-text"},{"data-hook":"review-body"}):
        	#print(rev_span)

                for rev_div2 in rev_span.find_all("div",{"class":"a-expander-collapsed-height a-row a-expander-container a-expander-partial-collapse-container"}):
                        #print(rev_div2)

                        for rev_div3 in rev_div2.find_all("div",{"class":"a-expander-content reviewText review-text-content a-expander-partial-collapse-content"}):
                                #print(rev_div3)

                                for rev_span2 in rev_div3.find_all("span"):
                                        #print(rev_span2.text)
                                        data1=rev_span2.text
					#data1.decode(errors='replace')
					data = data1.encode("utf-8")
					#data=unicode(data1,errors='ignore')	
					print(type(data))


                                        analysis = TextBlob(data)

					polarity = analysis.sentiment.polarity
					if(analysis.sentiment.polarity == 0):
						neutral +=1
					elif(analysis.sentiment.polarity < 0):
						negative +=1
					elif(analysis.sentiment.polarity > 0):
						positive +=1
					else:
						print("ERROR IN THE TEXTBLOB")
					i = i+1



#print("hello4")
				
#--------------------------------------------------------------------------------------------------------------------


"""		
		print('\n\n\n')
		print ("</br>")
		print ("</br>")	
		w1=rev_span.text
		w2=w1.encode("UTF-8")	
		
		print "hello",w2		
		#print(rev_span)

		analysis = TextBlob(rev_span.text)

		polarity +=analysis.sentiment.polarity
		if(analysis.sentiment.polarity == 0):
			neutral +=1
		elif(analysis.sentiment.polarity < 0):
			negative +=1
		elif(analysis.sentiment.polarity > 0):
			positive +=1
		else:
			print("ERROR IN THE TEXTBLOB")
		i = i+1
"""


			

pos=str(positive)
neg=str(negative)

neu=str(neutral)
star1=x1
star2=x2
star3=x3
star4=x4
star5=x5
print ("</br>")
print ("</br>")

#print "hello",type(w2)		


print("Priting the results for the reviews:")

print ("</br>")
print ("</br>")

print "NEUTRAL:",neutral
print ("</br>")
print "NEGATIVE:",negative
print ("</br>")
print "POSITIVE",positive
#print '\n\n',pos
#print type(pos)  
print('\n\n')
print ("</br>")

print ("</br>")
print '\n','1 star:',star1
print ("</br>")
print '\n','2 star:',star2
print ("</br>")
print '\n','3 star:',star3
print ("</br>")
print '\n', '4 star:',star4
print ("</br>")
print '\n','5 star:',star5




span2=str(span1)
k2=str(k1)
img2=str(img1)
print('<table style="border:1px solid black;width:100%;"><tr><td>'+span2+'</td><td><img style="" src="'+img2+'"></td></tr><tr><td>'+k2+'</td></tr></table>')




print('<center><h3><b><p> "Look at customer.html and star.html files for the visualized data!!" </h3></p></b>' )
#print ('<table style="border:1px solid black;width:100%;"><tr><td>'+span2+'"></td><td><img style="" src="'+img2+'"></td><td>'+k2+'</td></tr></table>')



#   print ('<a href="http://192.168.43.40s/cgi-bin/star.html">Star</a><br><a href="http://192.168.43.40/cgi-bin/customer.html">Customer review</a>"')



#       print ('<a href="file:///var/www/cgi-bin/customer.html">Star</a><br><a href="http://192.168.43.40/cgi-bin/customer.html">Customer review</a>"')

'''print("""
	<a href="file:///var/www/cgi-bin/star.html" target="_explorer.exe"> Star</a>


""")

'''

import time 

time.sleep(1)
names="file:///var/www/cgi-bin/star.html"
webbrowser.open_new_tab(names)




#file:///var/www/cgi-bin/customer.html
""""





			


#FOR THE BAR GRAPH Of reviews
left=[0.5,1.0,1.5]
height = [pos,neg,neu]
tick_label=['POSITIVE','NEGATIVE','NEUTRAL']
plt.bar(left,height,tick_label = tick_label,width=0.2,color=['yellowgreen','red','green'])
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()"""

			

		

#For the Pie Chart for reviews
fig1,y=plt.subplots()
#print ("hi")

labels=['Positive','Negative','Neutral']
sizes=[pos,neg,neu]
colors=['gold','yellowgreen','lightskyblue']
explode = (0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title('CUSTOMER REVIEW ANALYSIS')
plt.axis('equal')

mpld3.save_html(fig1,"customer.html")

"""



			
#for bar chart of star rating
left=[0.5,1.0,1.5,2.0,2.5]
height = [star1,star2,star3,star4,star5]
tick_label=['1 - STAR','2 - STAR','3 - STAR','4 - STAR','5 - STAR']
plt.bar(left,height,tick_label = tick_label,width=0.2,color=['yellowgreen','red','green','blue','orange'])
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()
"""

			
#print ("hello")
#For the Pie Chart for star
fig2,y=plt.subplots()
labels=['1 - STAR','2 - STAR','3 - STAR','4 - STAR','5 - STAR']
sizes=[star1,star2,star3,star4,star5]
colors=['gold','yellowgreen','lightskyblue','blue','red']
explode = (0.1,0,0,0,0)
plt.title("STAR RATING REVIEWS")
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.axis('equal')

mpld3.save_html(fig2,"star.html")



