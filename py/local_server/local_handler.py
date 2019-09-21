#!/usr/bin/env python3

import datetime
import json
from http import HTTPStatus
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from urllib import parse
import sys
sys.path.append("..")
from common.generic_server import Server
from local_server.local_commands import poll_for_updates
import local_server
PORT = 8000


class LocalRequestHandler(SimpleHTTPRequestHandler):
    # purpose:
    # 1. serve index.html
    # 2. respond to queries from index.html

    def do_GET(self):
        try:
            parsed = parse.urlparse(self.path)
            command_name = parsed.path[1:]
            params = parse.parse_qs(parsed.query)
            curtime = datetime.datetime.now()
            print('> {} Command: {}, parameters: {}'.format(curtime, command_name, params))

            if command_name == 'index':
                # return the index.html file
                print('<> Requested index; returning our page')
                self.path = '/index.html'
                return super(LocalRequestHandler, self).do_GET()
            else:
                print('> Polling for updates')
                result, code, content_type = poll_for_updates()
                print('< Update: {}'.format(result))
                self.send_response(code)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(json.dumps(result).encode('utf-8'))
        except Exception as e:
            print(e)
            self.send_error(HTTPStatus.NOT_FOUND, message=e.__str__())


if __name__ == '__main__':
    process = Thread(target=local_server.local_commands.check_green_button)
    process.start()
    Server('RPi server', LocalRequestHandler, PORT)
