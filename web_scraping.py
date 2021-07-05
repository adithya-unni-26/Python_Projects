#import required packages
from bs4 import BeautifulSoup
import requests
import csv 

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')# lxml is the script parser

#open a csv file and create a row using the writerow method
csv_file= open('/home/adi/projects/web_scraping.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Headline','Description', 'Youtube_link'])

#soup.findall returns a list of items with the matching tag
for article in soup.find_all('article'):

    title=article.h2.a.text # the title is obtained using the right tags.
    description = article.find('div', class_='entry-content').p.text#the class_ is used to narrow down the search
    #try and except is used because not all items have the iframe tag
    try:
        link= article.find('iframe', class_='youtube-player')['src']
        link_id =link.split('/')[4]
        link_id=link_id.split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={link_id}' # this is the common format of youtubelinks the id is extracted from the source and the link is created here 
    except Exception as e:
        youtube_link=None
    
    csv_writer.writerow([title,description,youtube_link])

    print(title)
    print()
    print(description)
    print()
    print(youtube_link)
    print()
    print()
csv_file.close()