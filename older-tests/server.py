
from http.server import HTTPServer, BaseHTTPRequestHandler


import socketserver
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from time import sleep

import random



# import socketserver.ThreadedHTTPServer
# from SocketServer import ThreadingMixIn
import threading


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        try:
            self.send_response(200)
            self.end_headers()

            c = getHtml()
            self.wfile.write(c)

            #self.wfile.write('\n')
        except:
            self.send_response(200)
            self.end_headers()
            b = bytearray()
            s = "error"
            b.extend(map(ord, s))
            self.wfile.write(b)
        return

    def do_POST(self):

        self.send_response(200)
        self.end_headers()

        message = threading.currentThread().getName()
        r = random.random()
        t = r * 30
        sleep(t)
        b = bytearray()
        s = message + " was sleepig " + str(t) + " seconds"
        print(s)
        b.extend(map(ord, s))
        self.wfile.write(b)

class ThreadedHTTPServer(socketserver.ForkingMixIn , HTTPServer):
    """Handle requests in a separate thread."""



def getHtml():

    p = "./client.html"
    file = open(p, 'rb')
    s = file.read()
    file.close()
    return s


if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()