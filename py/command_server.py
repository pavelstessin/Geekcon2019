from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse

PORT = 8000


class GeekconHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # self.request
        # self.client_address
        # self.server
        # parsed = urlparse(self.path)
        parsed = parse.urlparse(self.path)
        command_name = parsed.path[1:]
        params = parse.parse_qs(parsed.query)
        print('Command: {}, parameters: {}'.format(command_name, params))

        import commands
        # result = commands.get_project_name(params)

        method_to_call = getattr(commands, command_name)
        result = method_to_call(params)

        self.send_response(HTTPStatus.OK)
        # self.send_header("Content-type", 'application/json')
        self.send_header("Content-type", 'text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=GeekconHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)

    print('Serving on port {}'.format(PORT))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
