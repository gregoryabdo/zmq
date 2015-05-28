import zmq

def result_collector():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://localhost:5557")

    while True:
        print socket.recv_json()

result_collector()