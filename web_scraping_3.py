from bs4 import BeautifulSoup
import requests
import csv

csv_file= open('/home/adi/projects/web_scraping_3.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['JOBS','COMPANIES','LOCATIONS'])

url = requests.get('https://realpython.github.io/fake-jobs/').text
soup = BeautifulSoup(url,'lxml')

jobs= soup.find_all("h2", class_="title is-5")
companies=soup.find_all("h3", class_="subtitle is-6 company")
locations=soup.find_all("p", class_="location")


location=[k.text.strip() for k in locations]
job=[i.text for i in jobs]
company=[j.text for j in companies]

for i in range(len(location)):
    csv_writer.writerow([job[i],company[i],location[i]])

csv_file.close()
