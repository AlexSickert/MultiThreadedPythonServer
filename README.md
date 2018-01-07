# Multi Threaded Python Server

This is a little test that I made to check the performance of a socet server in combination with a Python Thread Pool. 

## Functionality:

When accessing the localhost:8888 in a browser, the browser will create a get request. The server responds to this get request by sending HTML code. The HTML code contains a JavaScript code. And this javascript code again produces a large quantity of POST requests. As AJAX works asynchonoously, the next AJAX call is made before the first returns. But doing this we can simulate heavy load on the server. In addition we track which of the threads handles how many requests. on the browser console the application then prints in intervals its restulst. 

## Example Console Output:

totalcount = 5005 speed (calls/second) = 484.1830318274161 parallelExec = 843 parallelCalls = 633
(index):95     Thread-15 = 311
(index):95     Thread-11 = 318
(index):95     Thread-4 = 333
(index):95     Thread-7 = 314
(index):95     Thread-14 = 317
(index):95     Thread-6 = 318
(index):95     Thread-10 = 308
(index):95     Thread-12 = 305
(index):95     Thread-2 = 316
(index):95     Thread-5 = 318
(index):95     Thread-13 = 311
(index):95     Thread-9 = 317
(index):95     Thread-1 = 443
(index):95     Thread-8 = 329
(index):95     Thread-3 = 318

The console output shows:

- 15 threads
- in total 5005 ajax post calls were made
- on average the server can handle 484 calls per second
- 843 ajax calls are waiting to finish. 

