#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "A message from CS381" to server, expects "Received by server" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Sending message...")
dict = {"Exercise":[["run", 30],["swim", 60]], "Work":[["Email", 90], ["Meetings", 120]], "Academics" : []}

socket.send_json(dict)

message = socket.recv_json()

print(type(message))
print(message)