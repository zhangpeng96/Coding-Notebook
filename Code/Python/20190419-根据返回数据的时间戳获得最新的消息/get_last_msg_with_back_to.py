import time, json


def getCurrentTime():
    return int(time.time())

def readJSON(path):
    with open(path) as f:
        contents = f.read()
    return json.loads(contents)

def ts2String():
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    return time_str

def getLastMsg(response, back_to):
    msg = []                        # 返回值list
    global last_order_time          # 调用全局变量
    last_order_time -= back_to      # 时间回溯，回溯时长要看修正值、back_to以及该函数具体调用的时间
    current_time = getCurrentTime() # 当前时间
    # 对传入数据按时间戳降序排序，避免后续更新last_order_time时出错
    response = sorted(response, key = lambda e: e.__getitem__('timestamp'), reverse = True)
    # 遍历传入数据
    for res in response:
        # 判断order_time是否大于current_time，若大于则将值束缚为current_time
        if res['timestamp'] > current_time:
            res['timestamp'] == current_time
        # 判断order_time是否大于last_order_time，若大于则说明是最新消息，追加到msg中，并更新last_order_time
        if res['timestamp'] > last_order_time:
            msg.append(res['text'])
            last_order_time = res['timestamp']
    # 返回msg
    return msg


if __name__ == '__main__':
    # 数据初始化
    # base_now = getCurrentTime()
    # response = [
    #     {"timestamp": base_now-10, "content": "最新消息"},
    #     {"timestamp": base_now+10, "content": "最新消息2"},
    #     {"timestamp": base_now+30, "content": "最新消息3"},
    #     {"timestamp": 1559619529, "content": "历史消息4"}
    # ]
    # 
    FIX_SECTION = 5                     # 定义修正值，使初始的last_order_time小于current_time某一个值
    last_order_time = getCurrentTime() - FIX_SECTION
    # 
    while (1):
        response = readJSON('test.json')
        msg = getLastMsg(response, 0)
        print(ts2String())
        print(msg)
        time.sleep(50)
