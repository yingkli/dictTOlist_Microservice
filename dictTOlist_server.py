#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects "A message from CS381 " from client, replies with "Received by server"
#

import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print(f"Received message from client:\n{message}")
    #dict = json.loads(message)
    print(type(message))
    #  Do some 'work'
    time.sleep(1)
    
    activity_list = []
    activity_time = []
    for key in message:
        activity_list.append(key)
        total_time = 0
        for item in message[key]:
            total_time += item[1]
        activity_time.append(total_time)
    activity = []
    activity.append(activity_list)
    activity.append(activity_time)
        #  Send reply back to client
    socket.send_json(activity)