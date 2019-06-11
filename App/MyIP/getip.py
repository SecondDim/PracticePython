#!/usr/bin/env python
#
# Gets your public IP address from a random server

try:  # Python 3
    import urllib.request as urlrequest
    import urllib.error
except ImportError:  # Python 2
    import urllib2 as urlrequest
from random import choice
from re import search

servers = [
    'http://ipecho.net/plain',          'http://websiteipaddress.com/WhatIsMyIp',
    'http://getmyipaddress.org/',       'http://myexternalip.com/raw',
    'http://www.canyouseeme.org/',      'http://www.trackip.net/',
    'http://icanhazip.com/',            'http://www.ipchicken.com/',
    'http://whatsmyip.net/',            'http://get.youripfast.com/',
    'http://ip-lookup.net/',            'http://checkip.amazonaws.com',
    'http://ipgoat.com/',               'http://www.myipnumber.com/my-ip-address.asp',
    'http://formyip.com/',              'https://check.torproject.org/',
    'http://www.displaymyip.com/',      'http://checkip.dyndns.com/',
    'http://myexternalip.com/',         'http://www.ip-adress.eu/',
    'https://wtfismyip.com/text',       'http://httpbin.org/ip'
]


def get():
    page = get_page(choice(servers))
    regex = 4 * '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    ip = search(regex.rstrip('\.'), str(page))

    if ip and ip.group:
        return ip.group(0)
    else:
        return get()


def get_page(url):
    try:
        req = urlrequest.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urlrequest.urlopen(req).read()
    except (urllib.error.HTTPError, urlrequest.HTTPError):
        return get_page(choice(servers))


if __name__ == '__main__':
    print(get())
