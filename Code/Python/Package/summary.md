# Python 各种包功能简述



### difflib

#### 两个文本文件对比实现

```python
import sys
import difflib

def GetLines(file_name):
    return open(file_name, encoding = 'utf-8').readlines()

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    report = sys.argv[3]
except Exception as e:
    print('Error:' + str(e))
    sys.exit()


txt_line1 = GetLines(file1)
txt_line2 = GetLines(file2)
d = difflib.HtmlDiff()
fid = open(report,'w', encoding = 'utf-8')
fid.write(d.make_file(txt_line1,txt_line2))
fid.close()
```



### plyer

#### PyPI 包安装

```shell
python -m pip install plyer
```

#### 操作系统级消息推送

```python
from plyer import notification

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
    timeout=10,  # seconds
)
```





