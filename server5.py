import socket

from  concurrent.futures import ThreadPoolExecutor
from time import sleep
import random
import threading

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

def getHtml():

    p = "./client.html"
    file = open(p, 'rb')
    s = file.read()
    file.close()
    return s

def handle_request(client_connection):
    request = client_connection.recv(1024)

    req = request.decode()
    print(req)

    if "GET /" in req:
        print("GET request")

        http_response = b"""\
HTTP/1.1 200 OK

            """
        http_response += getHtml()

    else:
        #print("POST request")

        http_response = b"""\
HTTP/1.1 200 OK

    """

        message = threading.currentThread().getName()

        b = bytearray()
        b.extend(map(ord, message))

        http_response += b

        #http_response += getHtml()

        # r = random.random()
        # t = r * 10
        # print("Thread " + str(message) + " goes to sleep for " + str(t) + " seconds")
        # sleep(t)
        # print("Thread " + str(message) + " woke up and returns after " + str(t) + " seconds")
        #
        # s = "HTTP/1.1 200 OK\n\n"
        # s += "Thread " + str(message) + " woke up and returns after " + str(t) + " seconds"
        #b = bytearray()
        #b.extend(map(ord, http_response))

        #http_response += b

        #print(b)

        #http_response = b


    # print(http_response)
    client_connection.sendall(http_response)
    client_connection.close()


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)

    executor = ThreadPoolExecutor(max_workers=15)

    print('Serving HTTP on port {port} ...'.format(port=PORT))

    while True:
        client_connection, client_address = listen_socket.accept()
        #handle_request(client_connection)

        a = executor.submit(handle_request, client_connection)


if __name__ == '__main__':
    serve_forever()