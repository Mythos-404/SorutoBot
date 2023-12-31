from flask import Flask
import json
import websocket
import threading
import os
import time
import yaml
import requests
import inspect
import sys


# 获取当前文件的父目录并切换工作目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
os.chdir(parent_directory)
sys.path.append(parent_directory)


from websocket_cli import WebsocketLink
from bridge.config import config
from bridge.load_plugins import plugin_loader

app = Flask(__name__)


@app.route('/load_plugins', methods=['GET'])
def loder_plugins():
    plugin_loader.load_plugins()
    time.sleep(0.1)
    return 'All plugins loaded.'


@app.route('/start_websocket', methods=['GET'])
def websocket_():
    connections = config["connections"]
    for connection_config in connections:
        # 来自文件 websocket_link
        websocket_ink = WebsocketLink(connection_config)
        t = threading.Thread(target=websocket_ink.run)
        t.daemon = True
        t.start()
    time.sleep(0.1)
    return 'All websockets connected.'


if __name__ == '__main__':
    # 检查是否有log文件夹
    if not os.path.exists('log'):
        os.mkdir('log')
    cd = 1
    print(f'[server] [Flask Watcher] reload: {config["server"]["reload"]}')

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true' or not config["server"]["reload"]:
        print(f'[server] 将在{cd}s后加载插件')
        print(f'[server] 将在{cd}s后唤醒ws连接')
        if config["server"]["webui"]:
            print(f'[server] [WebUI] on url: http://{config["server"]["host"]}:{config["server"]["local_port"]}/')
        else:
            print(f'[server] [WebUI] off')
        print(f'[server] [prefix] {config["bot"]["prefix"]}')
        print(f'[server] [rm_at] {config["bot"]["rm_at"]}')

        def start_ws():
            time.sleep(cd)
            requests.get(f'http://{config["server"]["host"]}:{config["server"]["local_port"]}/load_plugins')
            requests.get(f'http://{config["server"]["host"]}:{config["server"]["local_port"]}/start_websocket')

        t = threading.Thread(target=start_ws)
        t.daemon = True
        t.start()

    app.run(host=config["server"]["host"], port=config["server"]["local_port"], debug=config["server"]["reload"])







