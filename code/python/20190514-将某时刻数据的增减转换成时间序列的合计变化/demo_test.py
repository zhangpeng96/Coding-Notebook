import json, time

def whatever(data_dict, start_ts, end_ts, gap_ts):
    # 变量初始化
    i = 0
    value_count = 0
    result = []

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
        {'ts': 1009, 'value': 5},
        {'ts': 1022, 'value': 2},
        {'ts': 1024, 'value': 15},
        {'ts': 1029, 'value': 7},
        {'ts': 1030, 'value': 9}
    ]

    result = whatever(data, 1000, 1050, 3)
    print(json.dumps(result))
