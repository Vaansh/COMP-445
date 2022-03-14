#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import socket
import threading
from time import gmtime, strftime


class Server:
    methods = ["GET", "POST"]

    def __init__(self, port, directory):
        self.port, self.directory = port, directory
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.current_dir = os.getcwd() + "/httpfs"

    def serve(self):
        logging.info("STARTING: Web Server")
        try:
            self.listener.bind(("", self.port))
            self.listener.listen(1)
            for _ in Server.multi_client_loop():
                conn, addr = self.listener.accept()
                logging.debug(
                    "Recieved connection at address: {addr}".format(addr=addr[0])
                )
                threading.Thread(target=self.client_handler, args=(conn, addr)).start()
        finally:
            self.shut_server()

    def client_handler(self, conn, addr):
        try:
            request = conn.recv(1024).decode("utf-8").split("\r\n\r\n")
            h = request[0].split()
            method, path = h[0], h[1]
            
            req_body = request[1] if len(request) > 1 else None

            if method == self.methods[0]:
                logging.debug("Handling GET Request.")
                status, body = (
                    self.handle_empty_get()
                    if path == "/" or path == "HTTP/1.0"
                    else self.handle_normal_get(path)
                )
            elif method == self.methods[1] and req_body:
                logging.debug("Handling POST Request.")
                status, body = self.handle_post(path, req_body)
            else:
                logging.debug("Client made Bad Request.")
                status = Server.match_status(400)

            status = "HTTP/1.0 {status}".format(status=status)
            headers = "{status}Date: {current_time}Connection: close\r\n GMT\r\nServer: httpfs \r\nAccept-Ranges: bytes \r\nContent-Type: text \r\nContent-Length: {response_body_len}\r\n\r\n".format(
                status=status,
                current_time=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                response_body_len=str(len(body)),
            )

            response = Server.create_response(headers, body)
            conn.sendall(response.encode("utf-8"))
        finally:
            conn.close()
            logging.debug("Closed connection at address: {addr}".format(addr=addr[0]))

    def handle_empty_get(self):
        logging.debug("GET: Processing request to show directory")
        body = ""
        for sd, _, fs in os.walk(self.current_dir):
            for f in fs:
                body += (os.path.join(sd, f)) + "\n"
        status = Server.match_status(200)
        logging.debug("GET: Returning response with {status}".format(status=status[:3]))

        return status, body

    def handle_normal_get(self, path):
        path, body = self.current_dir + path, ""
        logging.debug("GET: Processing request to return content")
        try:
            if path.startswith(self.current_dir):
                with open(path, "r", encoding="utf-8") as f:
                    body = f.read()
                status = Server.match_status(200)
            else:
                raise ValueError("Forbidden")
        except ValueError:
            status = Server.match_status(403)
            logging.warning("Access Denied: Outside current directory")
        except IOError:
            status = Server.match_status(404)
            logging.warning("Not Found: No such directory/file")
        finally:
            logging.debug(
                "GET: Returning response with {status}".format(status=status[:3])
            )

        return status, body

    def handle_post(self, path, request_data):
        logging.debug("POST: Processing request to write to file")
        body, sep, check_access = "", path.split("/"), self.current_dir
        for i in range(len(sep) - 1):
            check_access += sep[i] + "/"

        try:
            if check_access.startswith(self.current_dir):
                path = self.current_dir + path
                with open(path, "w", encoding="utf-8") as f:
                    f.write(request_data)
                with open(path, "r", encoding="utf-8") as f:
                    body = "{0} created.\r\nSize : {1}\r\nContent: {{\r\n{2}\r\n}}\r\n".format(
                        sep[-1],
                        str(os.path.getsize(path)),
                        f.read(),
                    )
                status = Server.match_status(201)
                logging.debug("File Created: File creation successful")
            else:
                raise ValueError("Forbidden Directory")
        except ValueError:
            status = Server.match_status(403)
            logging.warning("Access Denied: Outside current directory")
        except IOError:
            status = Server.match_status(400)
            logging.warning("Not Found: No such directory/file")
        finally:
            logging.debug(
                "POST: Returning response with {status}".format(status=status[:3])
            )

        return status, body

    def shut_server(self):
        logging.info("STOPPING: Web Server")
        self.listener.close()
        logging.info("Shut web server at {port}.".format(port=self.port))

    # helper loop
    @staticmethod
    def multi_client_loop():
        while True:
            yield

    # helper response
    @staticmethod
    def create_response(headers, body):
        return headers + body

    # helper matcher
    @staticmethod
    def match_status(code):
        if code == 200:
            status = "200 OK"
        elif code == 201:
            status = "201 Created"
        elif code == 400:
            status = "400 Bad Request"
        elif code == 403:
            status = "403 Forbidden"
        elif code == 404:
            status = "404 Not Found"

        return status + "\r\n"
