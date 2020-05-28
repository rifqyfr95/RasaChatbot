from bs4 import BeautifulSoup
import csv
from csv import writer
from urllib.request import Request, urlopen
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

def fetch_unified_messaging_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")

    datax[row_px[0].text.strip()] = row_p[0].text.strip()
    container_fluid = soup.find("div",{"class":"container-fluid"})


    list_features = []

    row_title = container_fluid.findAll("h2")

    for title in row_title:
        datax[title.text.strip()] = ""
        list_features.append(title.text.strip())



    row_content = container_fluid.findAll("h3")
    n = 0
    for container in row_content:
        if n == 0:
            datax[list_features[0]] = container.text.strip()
        if n == 1:
            datax[list_features[1]] = container.text.strip()
        if n == 2:
            datax[list_features[2]] = container.text.strip()
        if n == 3:
            datax[list_features[4]] = container.text.strip()
        n = n + 1

    mini_dict = {}
    sub_list_features = []
    row_para = container_fluid.findAll("p")
    for container in row_para:
        data = container.findAll("span")[0].text.strip()
        sub_list_features.append(data)
        for span in container.findAll("span"):
            span.decompose()
        r = container.get_text().strip('\n').encode('utf-8')
        r = str(r)
        r = r.replace("b'", "")
        r = r.replace("'", "")
        r = r.strip()
        mini_dict[data] = r
    datax[list_features[3]] = mini_dict
    print(datax)
    # datax = [ast.literal_eval(i) for i in dict]

    with open('datacrawler.csv', 'w') as csvfile:
        fieldnames = ['Feature', 'Desc', 'Sub Features','Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': list_features[0], 'Sub Desc': datax[list_features[0]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': list_features[1], 'Sub Desc': datax[list_features[1]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': list_features[2], 'Sub Desc': datax[list_features[2]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': list_features[4], 'Sub Desc': datax[list_features[4]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': sub_list_features[0], 'Sub Desc': datax[list_features[3]][sub_list_features[0]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': sub_list_features[1], 'Sub Desc': datax[list_features[3]][sub_list_features[1]].replace(",",".")},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",","."), 'Sub Features': sub_list_features[2], 'Sub Desc': datax[list_features[3]][sub_list_features[2]].replace(",",".")},
                          ])

def fetch_live_streaming_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")

    list_features = []
    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").strip()
    container_fluid = soup.find("div",{"class":"container-fluid"})

    row_title = container_fluid.findAll("h2")
    row_content = container_fluid.findAll("h3")

    for title,content in zip(row_title,row_content):
        title = title.text.strip()
        content = content.text.replace(",", ".")
        content = content.replace("\n          ", "").strip()
        datax[title] = content
        list_features.append(title)


    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[0], 'Sub Desc': datax[list_features[0]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[1], 'Sub Desc': datax[list_features[1]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[2], 'Sub Desc': datax[list_features[2]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[3], 'Sub Desc': datax[list_features[3]].replace(",",".").strip()}
                          ])

def fetch_video_call_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")


    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").strip()
    container_fluid = soup.find("div",{"class":"container-fluid"})

    row_title = container_fluid.findAll("h2")
    row_content = container_fluid.findAll("h3")
    list_features = []

    for title,content in zip(row_title,row_content):
        title = title.text.strip()
        content = content.text.replace(",", ".")
        content = content.replace("\n          ", "").strip()
        list_features.append(title)
        datax[title] = content

    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[0], 'Sub Desc': datax[list_features[0]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[1], 'Sub Desc': datax[list_features[1]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[2], 'Sub Desc': datax[list_features[2]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[3], 'Sub Desc': datax[list_features[3]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[4], 'Sub Desc': datax[list_features[4]].replace(",",".").strip()}
                      ])


def fetch_audio_call_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")


    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").replace("\n      ","").strip()
    container_fluid = soup.find("div",{"class":"container-fluid"})

    row_title = container_fluid.findAll("h2")
    row_content = container_fluid.findAll("h3")
    list_features = []

    for title,content in zip(row_title,row_content):
        title = title.text.strip()
        content = content.text.replace(",", ".")
        content = content.replace("\n          ", "").strip()
        list_features.append(title)
        datax[title] = content

    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[0], 'Sub Desc': datax[list_features[0]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[1], 'Sub Desc': datax[list_features[1]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[2], 'Sub Desc': datax[list_features[2]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[3], 'Sub Desc': datax[list_features[3]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[4], 'Sub Desc': datax[list_features[4]].replace(",",".").strip()}
                      ])

def fetch_chat_bot_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")


    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").replace("\n      ","").replace("\n\t\t\t","").strip()
    container_fluid = soup.find("div",{"class":"container-fluid"})

    row_title = container_fluid.findAll("h2")
    row_content = container_fluid.findAll("h3")
    list_features = []

    for title,content in zip(row_title,row_content):
        title = title.text.strip()
        content = content.text.replace(",", ".")
        content = content.replace("\n          ", "").strip()
        list_features.append(title)
        datax[title] = content

    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[0], 'Sub Desc': datax[list_features[0]].replace(",",".").strip()},
                          {'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': list_features[1], 'Sub Desc': datax[list_features[1]].replace(",",".").strip()},
                          ])

def fetch_screen_share_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")


    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").replace("\n      ","").replace("\n\t\t\t","").strip()

    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'Feature': row_px[0].text.strip(), 'Desc': datax[row_px[0].text.strip()].replace(",",".").strip(), 'Sub Features': row_px[0].text.strip(), 'Sub Desc': datax[row_px[0].text.strip()].replace(",",".").strip()},
                          ])

def fetch_whiteboard_page(url: str):
    datax = {}
    req = Request(url, headers=hdr)
    html = urlopen(req,timeout=30)
    soup = BeautifulSoup(html, features="lxml")
    header_blocks = soup.find("header",{"class":"productBanner-alt"})
    row_px = header_blocks.findAll("h1")
    row_p = header_blocks.findAll("p")


    datax[row_px[0].text.strip()] = row_p[0].text.replace("\n        ","").replace("\n      ","").replace("\n\t\t\t","").strip()

    print(datax)

    with open('datacrawler.csv', 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        with open('datacrawler.csv', 'a+', newline='') as csvfile:
            # Create a writer object from csv module
            fieldnames = ['Feature', 'Desc', 'Sub Features', 'Sub Desc']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows([{'Feature': row_px[0].text.strip(),
                               'Desc': datax[row_px[0].text.strip()].replace(",", ".").strip(),
                               'Sub Features': row_px[0].text.strip(),
                               'Sub Desc': datax[row_px[0].text.strip()].replace(",", ".").strip()},
                              ])


url_um = "http://192.168.0.31/unifiedmessage.php"
url_ls = "http://192.168.0.31/livestream.php"
url_vc = "http://192.168.0.31/videocall.php"
url_ac = "http://192.168.0.31/audiocall.php"
url_wb = "http://192.168.0.31/whiteboard.php"
url_cb = "http://192.168.0.31/chatbot.php"
url_ss = "http://192.168.0.31/screenshare.php"

fetch_unified_messaging_page(url_um)
fetch_live_streaming_page(url_ls)
fetch_video_call_page(url_vc)
fetch_audio_call_page(url_ac)
fetch_chat_bot_page(url_cb)
fetch_screen_share_page(url_ss)
fetch_whiteboard_page(url_wb)



