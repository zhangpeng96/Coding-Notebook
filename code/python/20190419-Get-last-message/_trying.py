import time


# last_time = system_time
result = []

msg_dict = [{"time": 1555668228996, "content": "最新消息"}]


def getMST():    
    return int(time.time()*1000)

print(getMST())

# if system_time > (last_time + gap):
#     last_time = system_time - gap

# elif msg_dict[0]['time'] == last_time:
#     pass

# elif msg_dict[0]['time'] < last_time:
#     pass

# if msg_dict[0]['time'] > last_time:

#     for msg in msg_dict:
#         if msg['time'] <= last_time:
#             continue

#         result.append(msg['content'])

# last_time = msg_dict[0]['time']

# print(result)