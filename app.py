import os
from flask import Flask, jsonify, request
import requests
import json
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

@app.route("/")
def greet():
    data = """<h1> Welcome!</h1>
        <p> Noble here o/<br><br>go to /noble/api/login-status<br><br>or<br><br>
        /noble/api/game-status
    """
    return data

@app.route('/noble/api/login-status')
def get_data():
    return jsonify(login)

@app.route('/noble/api/game-status')
def get_data2():
    return jsonify(game_server)

if __name__ == '__main__':
    app.run()
