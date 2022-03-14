#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging
from server import Server


def main():
    help_map = {
        "v": "Prints debugging messages.",
        "p": "Specifies the port number that the server will listen and serve at. Default is 8080.",
        "d": "Specifies the directory that the server will use to read/write requested files. Default is the current directory when launching the application.",
    }

    parser = argparse.ArgumentParser(
        prog="httpfs",
        usage="httpfs [-v] [-p PORT] [-d PATH-TO-DIR]",
        description="httpfs is a simple file server.",
    )

    parser.add_argument("-v", help=help_map.get("v"), action="store_true")
    parser.add_argument("-p", help=help_map.get("p"), type=int, default=8080)
    parser.add_argument("-d", help=help_map.get("d"), default=".")

    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.v else logging.INFO)

    server = Server(args.p, args.d)
    server.serve()


if __name__ == "__main__":
    main()
