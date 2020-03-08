# Python 各种包功能简述



### plyer

#### PyPI

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



