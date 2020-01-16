import time, json, random

def getCurrentTime():
    return int(time.time())

def ts2String(timestamp):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    return time_str

def tprint(*param):
    text = ts2String(getCurrentTime())
    text += ' >'
    for p in param:
        text += ' ' + str(p)
    print(text)

def listShift(lst, new):
    lst.pop()
    lst.insert(0, new)
    return lst

def writeFile(path, json_obj):
    with open(path,'w') as f:
        f.write(json.dumps(json_obj))


if __name__ == '__main__':
    currentTs = getCurrentTime()
    data = [
        {'timestamp': currentTs-10, 'text': '消息时间 ' + ts2String(currentTs-10)},
        {'timestamp': currentTs-30, 'text': '消息时间 ' + ts2String(currentTs-30)},
        {'timestamp': currentTs-60, 'text': '消息时间 ' + ts2String(currentTs-60)},
        {'timestamp': currentTs-90, 'text': '消息时间 ' + ts2String(currentTs-90)},
        {'timestamp': currentTs-200, 'text': '消息时间 ' + ts2String(currentTs-200)}
    ]
    writeFile('test.json', data)
    
    while True:
        sleep_time = random.randint(10,70)
        tprint('下一次更新将在', sleep_time, '秒后')
        time.sleep(sleep_time)
        currentTs = getCurrentTime()
        rec = {'timestamp': currentTs, 'text': '消息时间 ' + ts2String(currentTs)}
        data = listShift(data, rec)
        tprint(data[0]['text'])
        writeFile('test.json', data)

