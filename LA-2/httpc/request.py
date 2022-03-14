#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import socket
from urllib.parse import urlparse


class Request:
    def __init__(self, url, port=80):
        self.url = urlparse(url)
        self.port = self.url.port if self.url.port else port
        self.host = self.url.hostname

        self.path = (
            "{0}?{1}".format(self.url.path, self.url.query)
            if self.url.query
            else self.url.path
        )

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def get(self, h="", o="", v=False):
        request = "GET {0} HTTP/1.0\r\nHost: {1}\r\n".format(self.path, self.host)
        if len(h) > 0:
            for x in h:
                request += "{0}\r\n".format(x)
        request += "\r\n"

        self.client.send(request.encode())
        response = self.client.recv(4096).decode("utf-8")

        self.log(response, o, v)

    def post(self, h="", d="", f="", o="", v=False):
        request = "POST {0} HTTP/1.0\r\nHost: {1}\r\n".format(self.path, self.host)
        if len(h) > 0:
            for x in h:
                request += "{0}\r\n".format(x)

        if len(d) > 0:
            tmp = d
        elif len(f) > 0:
            tmp = open(f, "r").read()
        request += "Content-Length: {0}\r\n\r\n{1}".format(str(len(tmp)), tmp)

        self.client.send(request.encode())
        response = self.client.recv(4096).decode("utf-8")

        self.log(response, o, v)

    def log(self, response, o="", v=False):
        _log = response if v else response.split("\r\n\r\n")[1]

        if len(o) > 0:
            f = open(o, "w")
            _break = "_"
            for _ in range(99):
                _break += "_"
            f.write(_log)
            f.write(_break)
            print("Response printed to " + o)
        else:
            print(_log)

    def end(self):
        self.client.close()
