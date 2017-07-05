import urllib, pyperclip, threading
from bs4 import BeautifulSoup


def saveAs(link, ftype):
    urllib.urlretrieve(link, ftype)

def crawl(soup,attr):
    for vid in soup.findAll(attrs={'class':attr})[0:1]:
        return vid['href']

def download(link):
    convertby = "https://www.youtubeinmp3.com/download/?video="
    attr = 'button'
    response=urllib.urlopen(link)
    soup = BeautifulSoup(response.read(),"html.parser")
    name=str(soup.find("title"))[7:-8]
    response=urllib.urlopen(convertby+urllib.quote(link))
    soup = BeautifulSoup(response.read(),"html.parser")
    div= crawl(soup,attr)
    downloadLink = 'https://www.youtubeinmp3.com'+div

    saveAs(downloadLink, name+'.mp3')


data=""
while True:
    data_new=pyperclip.paste()
    
    if(data_new!=data):
        data=data_new
        if("youtube.com" in data):
            try:
                downloader=threading.Thread(target=download(data))
            except Exception as e:
                print(str(e))
