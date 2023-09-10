import requests as req
import os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd',exist_ok = True)

n = input("Input the comic no.: ")
url += n
print('Downloading image from %s...' % url)
res = req.get(url).text
soup = bs4.BeautifulSoup(res,'lxml')
print(soup)

comicElem = soup.select('#comic img')
comicUrl = 'http:' + comicElem[0].get('src')
print(comicUrl)
res = req.get(comicUrl)

imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
for chunk in res.iter_content(1):
    imageFile.write(chunk)
imageFile.close()
print("Successfully downloaded")