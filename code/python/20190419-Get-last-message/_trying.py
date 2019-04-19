global last_time

last_time = system_time

def getLastMsg(msg_dict, system_time, gap):

    global last_time

    if system_time > (last_time + gap):
        last_time = system_time - gap

    elif msg_dict[0]['time'] == last_time:
        pass

    elif msg_dict[0]['time'] < last_time:
        pass

    if msg_dict[0]['time'] > last_time:

        for msg in msg_dict:
            if msg['time'] <= last_time:
                continue

            result.append(msg['content'])

    last_time = msg_dict[0]['time']
