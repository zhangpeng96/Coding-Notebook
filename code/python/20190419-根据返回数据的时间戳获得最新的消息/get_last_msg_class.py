import os, time, json


class Last():
    def __init__(self):
        self.__ts_key = 'timestamp'
        self.__fixed_gap = 5
        self.__last_rec_time = self.__currentTS() - self.__fixed_gap
        self.__lastest_list = []

    def __timeString(self, ts):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

    def __currentTS(self):    
        return int(time.time())

    def getNewMessage(self, record, backtime = 0):
        list_message = []
        list_timestamp = []
        self.__last_rec_time -= backtime
        current_time = self.__currentTS()
        for rec in record:
            rec_time = rec[self.__ts_key]
            if rec_time > current_time:
                rec_time = current_time
            if rec_time <= self.__last_rec_time:
                continue
            list_message.append(rec)
            list_timestamp.append(rec_time)
        if len(list_timestamp):
            self.__last_rec_time = max(list_timestamp)
        list_message.reverse()
        return list_message


def readJSON(path):
    with open(path) as f:
        contents = f.read()
    return json.loads(contents)

def ts2String():
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
    return time_str

if __name__ == '__main__':

    last = Last()

    # 数据回溯
    # while True:
    #     backtime = input('> ')
    #     response = readJSON('test.json')
    #     msg = last.getNewMessage(response, int(backtime))
    #     print(ts2String())
    #     print(msg)

    # 定时抓取最新数据
    while True:
        response = readJSON('test.json')
        msg = last.getNewMessage(response, 0)
        print(ts2String(), msg)
        time.sleep(30)
