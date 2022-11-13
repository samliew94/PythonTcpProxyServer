# PythonTcpProxyServer
A demo on developing a TCP proxy server that acts a middleman between a client and server 

## Demo is heavily based on LiveOverflow from https://www.youtube.com/watch?v=iApNzWZG-10

Demo details:
1. Demo is executed in localhost, including target destination.
2. Server listens at port 10000.
3. Client's original target destination would also be 10000.
4. We assume that the client's target destination has been modified via HOSTS file to point to proxy server listening at port 3333.

![Alt text](flow.png?raw=true "Title")

Steps highlighted in red refers to the flow:
1. Client sends a message "hello world" to the server running at port 10000.
2. Client's target destination has been changed to 3333, therefore Proxy Server intercepts receives the message.
3. Proxy server modifies the message to 'modified data' and forwards it to the actual Server.
4. Server sees the message 'modified data'.
5. Server responds with 'Sample Server Respond'
6. Proxy intercepts the Server respond and reads it as it is.
7. Proxy forwards the response to client.

END