
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
from time import sleep
import random
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

        message = threading.currentThread().getName()
        print("Thread " + str(message) + " goes to sleep")
        r = random.random()
        t = r * 30
        sleep(t)

        self.send_response(200)
        self.end_headers()
        b = bytearray()
        s = message + " was sleepig " + str(t) + " seconds"
        print(s)
        b.extend(map(ord, s))
        self.wfile.write(b)

def getHtml():

    p = "./client.html"
    file = open(p, 'rb')
    s = file.read()
    file.close()
    return s

if __name__ == '__main__':

    s = socketserver.ThreadingTCPServer(("localhost", 8080), Handler)
    socketserver.ThreadingTCPServer()
    try:
        print('Starting server 2, use <Ctrl-C> to stop')
        s.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        s.socket.close()
