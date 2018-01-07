

from http.server import HTTPServer, BaseHTTPRequestHandler, test

import socketserver

from http.server import  SimpleHTTPRequestHandler
#from SimpleHTTPServer import SimpleHTTPRequestHandler
from concurrent.futures import ThreadPoolExecutor # pip install futures

class PoolMixIn(socketserver.ThreadingMixIn):
    def process_request(self, request, client_address):
        self.pool.submit(self.process_request_thread, request, client_address)

def main():
    class PoolHTTPServer(PoolMixIn, HTTPServer):
        pool = ThreadPoolExecutor(max_workers=40)

    test(HandlerClass=SimpleHTTPRequestHandler, ServerClass=PoolHTTPServer)

if __name__=="__main__":
    main()

