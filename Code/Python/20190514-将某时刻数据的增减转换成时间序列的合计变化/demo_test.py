import json, time

def increment2TimeSeries(data_dict, start_ts, end_ts, gap_ts):
    # 变量初始化
    i = 0
    value_count = 0.0
    result = []
    # 数据按时间戳增加排序
    data_dict = sorted(data_dict, key = lambda e: e.__getitem__('ts'))
    # 生成时间序列
    for ts in range(start_ts, end_ts, gap_ts):
        while i < len(data_dict):
            # 避免下标越界
            if (data_dict[i]['ts'] >= ts and data_dict[i]['ts'] < (ts + gap_ts)):
                value_count += data_dict[i]['value']
                i = i + 1
            else:
                break
        # 追加数据
        result.append({'ts': ts + gap_ts - 1, 'value': value_count})

    return result


if __name__ == '__main__':

    data = [
        {'ts': 1009, 'value': 5.5},
        {'ts': 1029, 'value': 7.6667},
        {'ts': 1024, 'value': 15.75},
        {'ts': 1022, 'value': 2.3333},
        {'ts': 1030, 'value': 9.25}
    ]

    result = increment2TimeSeries(data, 1000, 1050, 3)
    print(json.dumps(result))
