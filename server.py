import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:4001")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    #  Do some 'work'
    time.sleep (1)        #   Do some 'work'
    #  Send reply back to client
    socket.send("World")
