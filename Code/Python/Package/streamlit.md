# streamlit

### 使用报错

```python
>>> import streamlit as st
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "\lib\site-packages\streamlit\__init__.py", line 103, in <module>
    from streamlit.delta_generator import DeltaGenerator as _DeltaGenerator
  File "\lib\site-packages\streamlit\delta_generator.py", line 25, in <module>
    from streamlit.proto import BlockPath_pb2
  File "\lib\site-packages\streamlit\proto\BlockPath_pb2.py", line 21, in <module>
    create_key=_descriptor._internal_create_key,
AttributeError: module 'google.protobuf.descriptor' has no attribute '_internal_create_key'
```

报错是因为`protobuf`包出错或版本不符，更新即可

```shell
$ pip install --upgrade protobuf
```

