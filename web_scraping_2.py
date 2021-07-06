import requests
from bs4 import BeautifulSoup
import csv 

csv_file= open('/home/adi/projects/web_scrapinng_2.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Publications','Subscribers'])


url=requests.get('https://toppubs.smedian.com/',timeout=10000).text
soup=BeautifulSoup(url,'lxml')

table=soup.find_all("div", class_="u-flex1 u-paddingRight5")

    
for tables in table:
    
    publication=tables.find("a",class_="heading link link--primary u-accentColor--hoverTextNormal u-displayInline").text
    subscribers=tables.find("a", class_="link u-colorLightGrey u-fontWeight400 u-fontSize14").text

    print(publication)
    print(subscribers)
    print()
    csv_writer.writerow([publication,subscribers.split()[0]])
    
csv_file.close()