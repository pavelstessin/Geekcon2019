from http.server import HTTPServer


class Server(object):

    def __init__(self, name, handler_class, port):
        self.name = name
        self.handler_class = handler_class
        self.port = port
        self._start()

    def _start(self):
        print('Starting server "{}" on port {}'.format(self.name, self.port))
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, self.handler_class)
        httpd.serve_forever()
