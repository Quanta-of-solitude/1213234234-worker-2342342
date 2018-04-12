import os
from flask import Flask, jsonify, request
import requests
import json
import time
import re
from bs4 import BeautifulSoup
app = Flask(__name__)

url = "{}".format(os.environ.get("server"))
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
g_data = soup.find_all("div", {"class": "server_wrap"})
login = []
count = 0
count2 = 0
game_server = []

#Soul worker------------------------------------------------------------------------
for x in g_data[1:7]:
    count +=1
    name_data = x.find("div", {"class": "server_name"}).get_text()
    last_offline = x.find("div", {"class": "last_offline_date"}).get_text()
    current_stats = x.find("div", {"class": "bit-3 current_status"}).get_text()
    current_stats = current_stats.replace("\n",'')
    login.append({"ID": count ,"name": name_data, "last_offline": last_offline, "current_status": current_stats})



for x in g_data[7:13]:
    count2 +=1
    name_data = x.find("div", {"class": "server_name"}).get_text()
    last_offline = x.find("div", {"class": "last_offline_date"}).get_text()
    current_stats = x.find("div", {"class": "bit-3 current_status"}).get_text()
    current_stats = current_stats.replace("\n",'')
    game_server.append({"ID": count2 ,"name": name_data, "last_offline": last_offline, "current_status": current_stats})
#Soul WOrker end-------------------------------------------------------------------------------------------------


@app.route("/")
def greet():
    data = """<h1> Welcome!</h1>
        <p> Noble here o/<br><br><br>go to /noble/api/login-status<br><br>or<br><br>
        /noble/api/game-status <strong>for soul worker stuff</strong><br><br>

        <br><br><br>This page is nub \o/<br></p>
    """
    return data

@app.route('/noble/api/login-status')
def get_data():
    return jsonify(login)

@app.route('/noble/api/game-status')
def get_data2():
    return jsonify(game_server)

'''@app.route('/noble/api/aq3d/item/<string:name>')
def get_data3(name):
    try:
        buggy = []
        link = "{}".format(os.environ.get("aqwiki"))
        name = name.replace(' ','-')
        name = name.replace("'", "-")
        name = name.replace("’", "-")
        name = name.lower()
        link = link+"{}".format(name)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        things = {}
        things["Text"] = soup.find("div", {"id": "page-content"}).get_text()
        things=dict(map(str.strip,x) for x in things.items())
        matcher = things["Text"].replace("\n\n","")
        pattern = re.compile("//<.*",re.DOTALL)
        m = pattern.findall(things["Text"])
        replacer = m
        if not m:
            new = things["Text"].replace("\n\n\n",'\n')

        else:
            new = things["Text"].replace(replacer[0], "----")
            new = new.replace("\n\n\n",'\n')

        k = json.dumps(new)
        l = json.loads(k)
        try:
            c = soup.find("img", alt=True,src=re.compile(r'\/i.imgur.com\/.+.png'))
            imgg = c['src']
        except:
            c = soup.find("img", alt=True, src=re.compile(r'\/local--files\/.+.png'))
            imgg = c['src']

        buggy.append({"data": l, "image": imgg})
        return jsonify(buggy)

    except:
        return jsonify({"error": "Not found XD"})'''



if __name__ == '__main__':
    while True:
        app.run()
        time.sleep(1800)
