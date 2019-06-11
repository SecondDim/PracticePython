import requests
from fake_useragent import UserAgent, FakeUserAgentError
from random import choice
from re import search
from retry import retry


class MyIP(object):

    ip = 'N/A'
    __servers = [
        'http://ipecho.net/plain',          'http://websiteipaddress.com/WhatIsMyIp',
        'http://getmyipaddress.org/',       'http://myexternalip.com/raw',
        'http://www.canyouseeme.org/',      'http://www.trackip.net/',
        'http://icanhazip.com/',            'http://www.ipchicken.com/',
        'http://whatsmyip.net/',            'http://get.youripfast.com/',
        'http://ip-lookup.net/',            'http://checkip.amazonaws.com',
        'http://ipgoat.com/',               'http://www.myipnumber.com/my-ip-address.asp',
        # 'http://formyip.com/',
        'https://check.torproject.org/',
        'http://www.displaymyip.com/',      'http://checkip.dyndns.com/',
        'http://myexternalip.com/',         'http://www.ip-adress.eu/',
        'https://wtfismyip.com/text',       'http://httpbin.org/ip',
        'https://www.whatismyip.com.tw/',   'https://whatismyipaddress.com/zh-cn/index',
        'https://myip.com.tw/',             'https://www.rus.net.tw/myip.php',
        'https://www.whois365.com/tw/',     'https://ifconfig.co/'
    ]

    def __init__(self,):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36'
        try:
            ua = UserAgent(path='tmp/fake_useragent.json')
            self.user_agent = ua.random
        except FakeUserAgentError:
            # TODO print WARING!
            pass

        self.headers = {'user-agent': self.user_agent}

        page = self.__request(choice(self.__servers))
        self.ip = self.__getIp(page)

    @retry(tries=3)
    def __request(self, url):
        r = requests.get(url, headers=self.headers)
        if r.ok:
            return r.text
        else:
            return '[x] Fail get server. server: %s' % url

    def __getIp(self, page):
        regex = 4 * r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
        ip = search(regex.rstrip(r'\.'), str(page))

        if ip and ip.group:
            return ip.group(0)
        else:
            return '[x] Fail get ip. server: %s' % page

    def test_servers(self,):
        for server in self.__servers:
            print(server)
            print(self.__getIp(self.__request(server)))


if __name__ == '__main__':
    # print(MyIP().ip)
    m = MyIP()
    m.test_servers()
