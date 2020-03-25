# FFmpeg 常用命令



### 时间调整

#### 拆分视频

首尾会自动寻找关键帧

-ss 开始时间 -t 持续时间

```bash
ffmpeg -ss 02:00:40 -t 0:01:44 -accurate_seek -i input.mp4 -codec copy -avoid_negative_ts 1 output.mp4
```
更多精确拆分的解释：<https://blog.csdn.net/matrix_laboratory/article/details/53157383>

#### 精确时间拆分视频

-ss 开始时间 -t 持续时间

```bash
ffmpeg -ss 0:0:2 -t 0:0:10 -accurate_seek -i input.mp4 -codec copy output.mp4
```



### 字幕相关

#### SRT字幕转ASS字幕
```bash
ffmpeg -i input.srt output.ass
```

#### 压制ass字幕

```bash
ffmpeg -i input.mp4 -vcodec libx264 -preset medium -crf 23 -vf "ass=input.ass" output.mp4
```

如果要由高分辨率低压缩的话用下面这句代码，其中Scale值：1080P对应1920，720P对应1280。

```bash
ffmpeg -i output.mp4 -vcodec libx264 -preset fast -crf 23 -vf "ass=input.ass,scale=1920:-1" output.mp4
```

##### 参数说明

`preset` - 编码速度，可选参数值如下：

`ultrafast` `superfast` `veryfast` `faster` `fast` `medium` `slow` `slower` `veryslow` `placebo`
默认值为`medium`，编码速度越慢文件大小会越小

`CFR` - 固定帧率 (constant rate factor)
无损：`0`、缺省值：`23`、最差：`51`、 一般选`18~28` 往往选`18`接近无损





### 视频调整

#### 无损旋转视频

逆时针旋转90°

```bash
ffmpeg -i input.mp4 -metadata:s:v rotate="90" -codec copy input.mp4
```





### 格式转换

#### 转换mkv至mp4

```bash
ffmpeg -i jr.mkv -y -vcodec copy -acodec copy jr.mp4
```
#### 转换webm至mp3

```bash
ffmpeg -i videoplayback.webm -acodec libmp3lame -aq 4 output.mp3
```
#### 无损转换flv至mp4

```bash
ffmpeg -i input.flv output.mp4
```



### 混缩与提取（无损）

### 合并音频和视频

```bash
ffmpeg -i video.mp4 -i audio.m4a -c:v copy output.mp4
```
#### 提取音频文件

```bash
ffmpeg -i input.mp4 -vn -acodec copy audio.m4a
```
#### 提取视频文件

```bash
ffmpeg -i input.mp4 -an -vcodec copy video.mp4
```

#### 提取字幕文件

```bash
ffmpeg -i input.mp4 -map 0:s:0 subtitle.srt
```

#### 获取多音轨视频文件的各个音轨

先用 FFmpeg 查看视频文件信息

```
# ffmpeg -i input.mpg 
Input #0, mpeg, from 'input.mpg ':  
  Duration: 00:00:32.32, start: 245.117611, bitrate: 8581 kb/s  
    Stream #0.0[0x1e0]: Video: mpeg2video, yuv420p, 720x480 [PAR 32:27 DAR 16:9], 9800 kb/s, 59.94 tbr, 90k tbn, 59.94 tbc  
    Stream #0.1[0x31]: Subtitle: dvdsub  
    Stream #0.2[0x81]: Audio: ac3, 48000 Hz, 5.1, s16, 384 kb/s  
    Stream #0.3[0x82]: Audio: ac3, 48000 Hz, 5.1, s16, 384 kb/s  
    Stream #0.4[0x80]: Audio: ac3, 48000 Hz, 5.1, s16, 448 kb/s  
    Stream #0.5[0x83]: Audio: ac3, 48000 Hz, stereo, s16, 160 kb/s  
    Stream #0.6[0x84]: Audio: ac3, 48000 Hz, stereo, s16, 160 kb/s  
    Stream #0.7[0x85]: Audio: ac3, 48000 Hz, stereo, s16, 192 kb/s  
    Stream #0.8[0x2d]: Subtitle: dvdsub  
    Stream #0.9[0x2e]: Subtitle: dvdsub  
    Stream #0.10[0x2f]: Subtitle: dvdsub  
    Stream #0.11[0x24]: Subtitle: dvdsub  
    Stream #0.12[0x30]: Subtitle: dvdsub  
    Stream #0.13[0x2a]: Subtitle: dvdsub  
    Stream #0.14[0x2b]: Subtitle: dvdsub  
    Stream #0.15[0x2c]: Subtitle: dvdsub  
    Stream #0.16[0x23]: Subtitle: dvdsub  
```

audio`%d`.wav (2-7) 即是输出的几个音轨的音频文件。
```bash
ffmpeg -i input.mpg -map 0:2 audio2.wav
ffmpeg -i input.mpg -map 0:3 audio3.wav
ffmpeg -i input.mpg -map 0:4 audio4.wav
...
ffmpeg -i input.mpg -map 0:7 audio7.wav
```




### 串流相关

#### 将rtmp流保存为视频

```bash
ffmpeg -i "rtmp://192.168.10.103:1935/live/111 live=1" -acodec copy -vcodec copy -f flv -y test.flv
```



### 屏幕录制

#### 录制当前屏幕

```bash
ffmpeg -f gdigrab -framerate 10 -i desktop output.mkv
```

#### 录制指定窗口

比如录制计算器 Calculator

```bash
ffmpeg -f gdigrab -framerate 25 -i title=Calculator output.mkv
```





### 参考链接

- ffmpeg linux 命令 在线中文手册：<http://linux.51yip.com/search/ffmpeg>
- https://blog.csdn.net/achang21/article/details/49128785