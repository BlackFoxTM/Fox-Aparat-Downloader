import requests 
from tqdm import tqdm
from pyfiglet import Figlet
import rainbowtext
import colorama
import re

def banner():
    figlet = Figlet(font="small").renderText("Fox Aparat")
    return rainbowtext.text(figlet)
url_lists = []
quality = []
def cookie():
    with requests.Session() as session:
        url = "https://www.aparat.com/user/profile/ping_afcn"
        session.headers.update({"isnext":True})
        header = requests.get(url).headers.get("Set-Cookie")
        return header

def download_list(urlx):
    with requests.Session() as session:
        url = f"https://www.aparat.com/api/fa/v1/video/video/show/videohash/{urlx}?pr=1&mf=1&referer=direct"
        session.headers.update({"Cookie":cookie() , "Isnext":"True"})
        data = session.get(url).json()
        for datas in data['data']['attributes']['file_link_all']:
            url_lists.append(datas['urls'][0])

def quality_list():
    download_list(urlx)
    for url_list in url_lists:
        if "144p" in url_list:
            quality.append("144")
        if "240p" in url_list:
            quality.append("240")
        if "360p" in url_list:
            quality.append("360")
        if "480p" in url_list:
            quality.append("480")
        if "720p" in url_list:
            quality.append("720")
        if "1080p" in url_list:
            quality.append("1080")

def number_download():
    quality_list()
    number_to_download = len(quality)
    if number_to_download == 1:
        num = input(rainbowtext.text("Quaility : [1] - 144\n\n~ Select an Option :  "))
    elif number_to_download == 2:
        num = input(rainbowtext.text("[1] - 144p\n[2] - 240p\n\n~ Select an Option : "))
    elif number_to_download == 3:
        num = input(rainbowtext.text("[1] - 144p\n[2] - 240p\n[3] - 360p\n\n~ Select an Option : "))
    elif number_to_download == 4:
        num = input(rainbowtext.text("[1] - 144\n[2] - 240p\n[3] - 360\n[4] - 480p\n\n~ Select an Option : "))
    elif number_to_download == 5:
        num = input(rainbowtext.text("[1] - 144p\n[2] - 240p\n[3] - 360p\n[4] - 480p\n[5] - 720p\n\n~ Select an Option : "))
    elif number_to_download == 6:
        num = input(rainbowtext.text("[1] - 144[\n[2] - 240p\n[3] - 360p\n[4] - 280p\n[5] - 720p\n[6] - 1080p\n\n~ Select an Option : "))

    final = int(num) - 1
    return url_lists[final]
        
def finaly():
    url = number_download()
    req = requests.get(url , stream=True)
    total_size_in_bytes= int(req.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open("saved.mp4","wb") as file:
        for data in req.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    rainbowtext.text("The Operation Has been success !")
    print (colorama.Fore.WHITE)
print (banner())
xurl = input(rainbowtext.text("Please Enter your video url -> "))
urlx = re.split(r".*aparat.com/v/" , xurl)[1].split("/")[0]
finaly()
