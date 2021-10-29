import requests
from bs4 import BeautifulSoup

#enter link

url = "https://imsdb.com/scripts/Next.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

end = url[26::]
title = end.replace('.html','')
title = title.replace('-','')
title = title.replace('_','')

for x in soup.findAll('td', {'class','scrtext'}):
    data = x.text
    print(data)

with open('C:/Users/anedj/Desktop/' + title + '.text', 'w') as f:
    f.write(data)