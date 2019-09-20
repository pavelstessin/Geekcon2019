import datetime
from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse

import commands

PORT = 8000


class GeekconHTTPRequestHandler(SimpleHTTPRequestHandler):

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
                return super(GeekconHTTPRequestHandler, self).do_GET()
            else:
                method_to_call = getattr(commands, command_name)
                result, code, content_type = method_to_call(params)
                curtime = datetime.datetime.now()
                print('< {} Command: {}, parameters: {}, got result: {}\n'.format(curtime, command_name, params, result))

                self.send_response(HTTPStatus.OK)
                # self.send_header("Content-type", 'application/json')
                self.send_header("Content-type", 'text/plain')
                self.end_headers()
                self.wfile.write(result.encode('utf-8'))
        except Exception as e:
            print(e)
            self.send_error(HTTPStatus.NOT_FOUND, message=e.__str__())


def run(server_class=HTTPServer, handler_class=GeekconHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)

    print('Serving on port {}'.format(PORT))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
