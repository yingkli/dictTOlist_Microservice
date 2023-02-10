#
#   dictTolist client in Python
#   Connects REQ socket to tcp://localhost:5560
#   Sends activity dictionary to server, expects "Received by server" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5560")

# sending request (sample activity dictionary) to server
print("Sending activity dictionary...")
activity_dict = {"Exercise":[["run", 30],["swim", 60]], "Work":[["Email", 90], ["Meetings", 120]], "Academics" : []}
socket.send_json(activity_dict)

# receive reply from server
activity_list = socket.recv_json()
print(f"Received reply from server\n{activity_list}")