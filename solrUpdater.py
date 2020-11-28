#!/usr/bin/env python

from __future__ import print_function
import json
import socket
import sys
import requests
import argparse
import time

try:
    from urllib.request import urlopen # Python 3.x
except ImportError:
    from urllib2 import urlopen # Python 2.7


def getCoresList(url):
    response = urlopen(url)

    if(response.getcode()==200):
        data = response.read().decode("utf-8")
        jsonData = json.loads(data)
    else:
        print("Error receiving data", response.getcode())

    return jsonData


def updateCore(name,ip, mode, debug, wait):

    params = (
        ('command', mode),
    )

    print('Update {} started...'.format(name))
    try:
        response = requests.get('http://{}:8983/solr/{}/dataimport'.format(ip,name), params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    print('[status] {} {}\n'.format(response.status_code,response.reason))
    if debug:
        print('[debug] {}\n'.format(response.text))

    time.sleep(wait)

if __name__ == '__main__':
    print("[log] SolrUpdater started\n")

    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='127.0.0.1', help="Solr serwer ip adres (default: 127.0.0.1)")
    parser.add_argument('--mode', type=str, default='delta-import', help="Import mode: delta-import, full-import (default: full-import)")
    parser.add_argument('--wait', type=int, default=0, help="Time between update next core (default: 0s)")
    parser.add_argument('--debug', help="Show full response", action="store_true")
    args = parser.parse_args()

    if args.ip:
        ip = args.ip
    else:
        ip = '127.0.0.1'

    if args.debug:
        debug = args.debug
    else:
        debug = False

    if args.wait:
        wait = args.wait
    else:
        wait = 0

    url = ("http://{}:8983/solr/admin/cores?action=STATUS").format(ip)
    jsonData = getCoresList(url)

    for core in jsonData["status"]:
        updateCore(core, ip, args.mode, debug, wait)

    print('[log] That\'s all')
