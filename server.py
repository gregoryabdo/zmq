import zmq
import time
import random

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://localhost:5557")

    # Start your result manager and workers before you start your producers
    while True:
        zmq_socket.send_json({'num': random.randrange(1,215)})
        time.sleep(1)

producer()
