#! python3

"""
python-dotenv
https://github.com/theskumar/python-dotenv
"""
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import requests
import os

"""
發送 Line Notify 訊息
http://pythonorz.blogspot.tw/2017/12/python-line-notify-line-notify-line.html
"""


def lineNotify(token, msg):

    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code


def run():

    # TOKEN = os.environ.get("TOKEN01")#self
    TOKEN = os.environ.get("TOKEN02")  # CCLAB106
    msg = "test"
    lineNotify(TOKEN, msg)


if __name__ == '__main__':

    run()
    print("DONE")
    # input("DONE")
