import datetime
import json
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from urllib import parse

from common.generic_server import Server
from remote_server import remote_commands

PORT = 9000


class RemoteRequestHandler(SimpleHTTPRequestHandler):
    # purpose:
    # 1. serve requests to generate project names

    def do_GET(self):
        try:
            parsed = parse.urlparse(self.path)
            command_name = parsed.path[1:]
            params = parse.parse_qs(parsed.query)
            curtime = datetime.datetime.now()
            print('> {} Command: {}, parameters: {}'.format(curtime, command_name, params))

            result, code, content_type = getattr(remote_commands, command_name)(params)
            self.send_response(code)
            self.send_header("Content-type", content_type)
            self.end_headers()
            self.wfile.write(json.dumps(result).encode('utf-8'))
        except Exception as e:
            print(e)
            self.send_error(HTTPStatus.NOT_FOUND, message=e.__str__())


if __name__ == '__main__':
    Server('Remote project server', RemoteRequestHandler, PORT)
