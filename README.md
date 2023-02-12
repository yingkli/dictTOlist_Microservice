# dictTOlist_Microservice
This microservice will receive an activity dictionary in following example format:
{'Exercise': [['run', 30], ['swim', 60]], 'Work': [['Email', 90], ['Meetings', 120]], 'Academics': []}
and will extract the keys (which are activity catogories) and summary total time spent for each activity catogory. 
The microservice will reply with a list containing the above info in example format:
[['Exercise', 'Work', 'Academics'], [90, 210, 0]]



How to request data:
The communication pipe uses ZeroMQ. The client has to make sure to import this module first.
The client will then create socket and build connection to the server. The address is "tcp://localhost:5560"
After connecting to server, the client can then send the request, which is the activity dictionary to the server by using json format. 
For detailed info, please refer to the example call.

###############
# EXAMPLE CALL

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
###############



How to receive data: 
The reply, which is a list, will be sent from server in json format. The client can receive it using socket.recv_json() function.
Following is an example:

###############
# receive reply from server
activity_list = socket.recv_json()
print(f"Received reply from server\n{activity_list}")
###############



UML sequence diagram:

dictTOlist server                             client
<img width="852" alt="image" src="https://user-images.githubusercontent.com/62686741/218289815-f46144e1-f2a1-4397-901a-bb57ac25e4c0.png">
