#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse
from request import Request


def main():
    parser = argparse.ArgumentParser(
        description="Http parser", conflict_handler="resolve"
    )

    parser.add_argument("cmd", choices=["get", "post", "help"])
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-h", dest="headers", nargs="+")
    parser.add_argument("-d", dest="data", action="store", metavar="inline-data")
    parser.add_argument("-f", dest="file", action="store")
    parser.add_argument("URL", type=str, nargs="?", action="store", default="")
    parser.add_argument("-o", dest="output", action="store")

    args = parser.parse_args()
    check_args(args)


def check_args(args):
    if args.cmd == "get" and (args.data or args.file):
        print("ERROR: GET cannot be used with -d or -f flags.")
        return
    elif args.cmd == "post" and (args.data and args.file):
        print("ERROR: POST cannot be used with both -d and -f flags.")
        return

    headers = args.headers
    if headers:
        for h in headers:
            if not ((h[1:len(h) - 1].count(":") == 1) and (":" not in [h[0], h[len(h) - 1]])):
                print("ERROR: [Header: {0}] -h flag must follow the following format: (key:value)*.".format(h))
                return

    make_request(args)


def make_request(args):
    request = Request(args.URL)

    help_menu = """httpc is a curl-like application but supports HTTP protocol only.\nUsage:
    httpc command [arguments] \nThe commands are:
    get     executes a HTTP GET request and prints the response. 
    post    executes a HTTP POST request and prints the response.
    help    prints this screen.\nUse "httpc help [command]" for more information about a command."""

    get_usage = """usage: httpc get [-v] [-h key:value] URL\nGet executes a HTTP GET request for a given URL.
    -v  Prints the detail of the response such as protocol, status, and headers.
    -h  key:value Associates headers to HTTP Request with the format "key:value"."""

    post_usage = """usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL\nPost executes a HTTP POST request for a given URL with inline data or from file.
    -v  Prints the detail of the response such as protocol, status, and headers.
    -h  key:value Associates headers to HTTP Request with the format "key:value".
    -d  string Associates an inline data to the body HTTP POST request.
    -f  file Associates the content of a file to the body HTTP POST request.\nEither [-d] or [-f] can be used but not both."""

    invalid_input = """Invalid input. Enter one of the following commands to learn more about them: { get, post }"""

    message_map = {"": help_menu, "get": get_usage, "post": post_usage}

    if args.cmd == "get":
        request.get(
            h = "" if not args.headers else args.headers,
            o = "" if not args.output else args.output,
            v = args.verbose,
        )
    elif args.cmd == "post":
        request.post(
            h = "" if not args.headers else args.headers,
            d = "" if not args.data else args.data,
            f = "" if not args.file else args.file,
            o = "" if not args.output else args.output,
            v = args.verbose,
        )
    elif args.cmd == "help":
        print(message_map.get(args.URL, invalid_input))

    request.end()

if __name__ == "__main__":
    main()