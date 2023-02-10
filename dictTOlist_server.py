#
#   dictTolist server in Python
#   Binds REP socket to tcp://*:5560
#   Expects an activity dictionary from client, replies with a list with activity category and total time spent
#   Example format of dictionary: 
#   {"Exercise":[["run", 30],["swim", 60]], "Work":[["Email", 90], ["Meetings", 120]], "Academics" : []}
#   Example format of list reply:
#   [["Exercise", "Work", "Academics"],[90, 210, 0]]



import time
import zmq
import json

# binds socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5560")

while True:
    #  Wait for next request from client
    activity_dict = socket.recv_json()
    print(f"Received message from client:\n{activity_dict}")
 
    time.sleep(1)
    
    # create reply list
    activity = []
    # create sublists in reply list
    activity_list = []
    activity_time = []
    # find all activity categories (keys) in the dictionary
    for key in activity_dict:
        activity_list.append(key)
        total_time = 0
        # for each activity category (key), sub total time spent for it
        for item in activity_dict[key]:
            total_time += item[1]
        activity_time.append(total_time)
    # append sublists to the reply list
    activity.append(activity_list)
    activity.append(activity_time)
    
    #  Send reply back to client
    print("Sending reply to client...")
    socket.send_json(activity)