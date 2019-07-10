import os, time, json


class Last():
	# 初始化数据
    def __init__(self):
        self.__ts_key = 'timestamp'		# 传入的JSON数据中时间戳的KeyName
        self.__fixed_gap = 5			# 当前时间修正值，可设置为一个不为零较小的整数
        self.__last_rec_time = self.__currentTS() - self.__fixed_gap
    # 获得当前时间戳
    def __currentTS(self):    
        return int(time.time())
    # 获得更新的最新数据
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


if __name__ == '__main__':

	'''
	  辅助测试用函数
	'''
	def readJSON(path):
	    with open(path) as f:
	        contents = f.read()
	    return json.loads(contents)

	def ts2String():
	    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))
	    return time_str
    
	'''
	  实例化类
	'''
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
        msg = last.getNewMessage(response)
        print(ts2String(), msg)
        time.sleep(30)
