# FFmpeg 常用命令

### FFmpeg 常见参数

- `-i` - 输入文件（路径）
- `-y` - 覆盖输出文件



### 格式转换

#### FLV 转换为 MP4

```bash
$ ffmpeg -i "input.flv" "output.mp4"
```

#### WEBM 转换为 MP3

```bash
$ ffmpeg -i "input.webm" -acodec libmp3lame -aq 4 "music.mp3"
```

#### 无损转换

无损转换是将视频的视频流、音频流直接复制而不经过编码器再次编码，直接由指定的容器格式封装。

如 MKV 转换为 MP4

```bash
$ ffmpeg -i "input.mkv" -y -vcodec copy -acodec copy "output.mp4"
```

- `-vcodec copy` - 复制视频流
- `-acodec copy` - 复制音频流

另外`-vcodec`、`-acodec`可以分别写作`-c:v`、`-c:a`，因此上面的命令还可以写成

```bash
$ ffmpeg -i "input.mkv" -c:v copy -c:a copy "output.mp4"
```

还能进一步简写成`-c copy`

```bash
$ ffmpeg -i "input.mkv" -c copy "output.mp4"
```



### 时间调整

#### 剪切视频（无损）

普通剪切方法首尾会自动寻找关键帧，因此剪切的时间并不一定准确

假设剪切`input.mp4`文件，从 22:23 开始，截取 2:50 长的内容：

```bash
$ ffmpeg -ss 00:22:23 -i "input.mp4" -t 00:02:50 -c:v copy -c:a copy "output.mp4"
```
- `-ss` - 开始时间
- `-t` - 持续时间
- 以上时间格式既可以使用整数表示秒，也可以以`hh:mm:ss.microsecond`方式表达

如果不用时长，而是指定截取的结束时间位置，这时要使用`-to`参数

```bash
$ ffmpeg -ss 00:22:23 -i "input.mp4" -to 00:25:13 -c:v copy -c:a copy -copyts "output.mp4"
```

- `-to` - 截止时间
- `-copyts` - 复制文件的时间戳，注意该指令一定要有，否则将会出错

**注意 FFmpeg 关于参数位置的问题**

FFmpeg 与大多数命令行不同，各个参数位置的调整可能会引发错误，因此上述时间调整命令的参数尽量不要改动，详细查看参考链接。

#### 精准剪切视频（无损）

如果需要准确定位时间，应在`-i`前加`-accurate_seek`

```bash
$ ffmpeg -ss 00:22:23 -accurate_seek -i "input.mp4" -t 00:02:50 -c:v copy -c:a copy -avoid_negative_ts 1 "output.mp4"
```
- `-avoid_negative_ts 1` - 由于视频通常是帧间编码，某一帧依赖于其它帧的解码，因此当直接复制视频流时可能会将依赖的帧剪入，设置该项为1可以避免这些问题



### 视频画面调整

#### 无损旋转视频

逆时针旋转 90°

```bash
$ ffmpeg -i "input.mp4" -metadata:s:v rotate="90" -c:v copy -c:a copy "output.mp4"
```



### 字幕相关

#### SRT 字幕转换为 ASS 字幕
```bash
$ ffmpeg -i "input.srt" "output.ass"
```

#### 压制 ASS 字幕（硬字幕）

```bash
$ ffmpeg -i "input.mp4" -vf "ass=input.ass" "output.mp4"
```

注意，不添加具体的参数直接压入字幕时 FFmpeg 可能会用缺省质量参数，因此视频质量会有明显下降，可以用下面代码调整质量，其中 scale 值：1080P 对应 1920，720P 对应 1280。

```bash
$ ffmpeg -i "input.mp4" -vcodec libx264 -preset fast -crf 23 -vf "ass=input.ass,scale=1920:-1" "output.mp4"
```

- `-preset` - 编码速度，可选参数值如：`ultrafast` `superfast` `veryfast` `faster` `fast` `medium` `slow` `slower` `veryslow` `placebo`， 默认值为`medium`，编码速度越慢文件大小会越小

- `-crf` - 固定帧率 (constant rate factor)，无损：`0`、缺省值：`23`、最差：`51`、 一般选`18~28` 往往选`18`接近无损



### 合并或提取音视频、字幕等轨道

#### 合并音视频轨道

```bash
$ ffmpeg -i "video.mp4" -i "audio.m4a" -c copy "output.mp4"
```
#### 提取音频文件

```bash
$ ffmpeg -i "input.mp4" -vn -acodec copy "audio.m4a"
```
#### 提取视频文件

```bash
$ ffmpeg -i "input.mp4" -an -vcodec copy "video.mp4"
```

#### 提取字幕文件

```bash
$ ffmpeg -i "input.mp4" -map 0:s:0 "subtitle.srt"
```

#### 获取多轨道视频文件的各个轨

先用 FFmpeg 查看视频文件信息

```bash
$ ffmpeg -i "input.mpg" 
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
$ ffmpeg -i input.mpg -map 0:2 audio2.wav
$ ffmpeg -i input.mpg -map 0:3 audio3.wav
$ ffmpeg -i input.mpg -map 0:4 audio4.wav
...
$ ffmpeg -i input.mpg -map 0:7 audio7.wav
```

#### 将图片和音频合成为视频

```bash
$ ffmpeg -f image2 -i "image.jpg" -i "audio.aac" -acodec copy "output.mp4"
```

但是这种方法转换后视频轨大概率是无效的，比如b站上传后转码失败，因此建议使用下面的方法：

```bash
$ ffmpeg -r 15 -f image2 -loop 1 -i "image.jpg" -i "audio.aac" -acodec copy -t 442 "output.mp4"
```

- `-r` - 转换视频的帧率，默认为`25`
- `-loop 1` - 因为只有一张图片所以必须加入这个参数
- `-t` - 转换成的视频持续时长（单位是秒），必须指定该值，否则会无限制生成视频

如果要用多图片组合成视频，输入路径可以用占位符`image%03d.jpg`



### 流媒体相关

#### 将 RTMP/m3u8 流保存为视频

```bash
$ ffmpeg -i "rtmp://192.168.10.103:1935/live/stream" -acodec copy -vcodec copy -absf aac_adtstoasc "output.mp4"
```

- `-absf aac_adtstoasc` - 流媒体参数转换，建议保留

> aac_adtstoasc 是 将 AAC 编码器编码后的原始码流（ADTS 头 + ES 流）封装为 MP4、FLV 或 MOV 等格式时，需要先将 ADTS 头转换为 MPEG-4 AudioSpecficConfig（将音频相关编解码参数提取出来），并将原始码流中的 ADTS 头去掉（只剩下 ES 流）。相反，从 MP4 或者 FLV 或者 MOV 等格式文件中解封装出 AAC 码流（只有 ES 流）时，需要在解析出的 AAC 码流前添加 ADTS 头（含音频相关编解码参数）。

#### 对直播流截图

以下指令可以对直播流截图，但是由于直播是持续的，截图得到的指令发出时的图片

```bash
$ ffmpeg -i "rtmp://192.168.10.103:1935/live/stream" "screenshot.jpg"
```
如果要连续截图需要在输出图片名中指定连续格式，如`%03d`表示从命名从`001`开始，不足3位以0补齐
```bash
$ ffmpeg -i "rtmp://192.168.10.103:1935/live/stream" "screenshot-%03d.jpg"
```
需要注意的是连续截图是以视频源的每一帧为单位截图，因此会产生大量图片

如果只是要间隔几秒截图可以用视频滤镜调节帧率  `-vf fps=0.1`，这里`fps=0.1`的效果就是每 10 秒截图一次

```bash
$ ffmpeg -i "rtmp://192.168.10.103:1935/live/stream" -vf fps=0.1 "screenshot-%03d.jpg"
```

有时候不需要输出大量的图片序列，而是在原来的文件基础上覆盖，可以设置`-update`参数

```bash
$ ffmpeg -i "rtmp://192.168.10.103:1935/live/stream" -vf fps=0.1 -update 1 -y "screenshot.jpg"
```

- `-update 1` - 更新（覆盖）输出文件，注意参数值 1 是必须填写的，是布尔值表示该参数有效
- `-y` - 直接覆盖同名文件不再询问



### 屏幕录制

#### 录制当前屏幕

```bash
$ ffmpeg -f gdigrab -framerate 10 -i desktop "output.mkv"
```
- `framerate` - 录屏的帧率

#### 录制指定窗口

比如录制计算器 Calculator

```bash
$ ffmpeg -f gdigrab -framerate 25 -i title=Calculator "output.mkv"
```



### 使用硬件加速

如果电脑有独立显卡或某些显卡支持渲染加速，那么就可以用显卡对 FFmpeg 编码加速，加快视频编码的速度，减轻 CPU 的负担。

对于 Windows 系统，可以在 PowerShell 中查看当前 FFmpeg 和设备支持的编码器、解码器

```powershell
PS ffmpeg -codecs | sls cuvid
 DEV.LS h264                 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (decoders: h264 h264_qsv h264_cuvid ) (
encoders: libx264 libx264rgb h264_amf h264_nvenc h264_qsv nvenc nvenc_h264 )
 DEV.L. hevc                 H.265 / HEVC (High Efficiency Video Coding) (decoders: hevc hevc_qsv hevc_cuvid )
 (encoders: libx265 nvenc_hevc hevc_amf hevc_nvenc hevc_qsv )
 DEVIL. mjpeg                Motion JPEG (decoders: mjpeg mjpeg_cuvid mjpeg_qsv ) (encoders: mjpeg mjpeg_qsv )
 DEV.L. mpeg1video           MPEG-1 video (decoders: mpeg1video mpeg1_cuvid )
 DEV.L. mpeg2video           MPEG-2 video (decoders: mpeg2video mpegvideo mpeg2_qsv mpeg2_cuvid ) (encoders: m
peg2video mpeg2_qsv )
 DEV.L. mpeg4                MPEG-4 part 2 (decoders: mpeg4 mpeg4_cuvid ) (encoders: mpeg4 libxvid )
 D.V.L. vc1                  SMPTE VC-1 (decoders: vc1 vc1_qsv vc1_cuvid )
 DEV.L. vp8                  On2 VP8 (decoders: vp8 libvpx vp8_cuvid vp8_qsv ) (encoders: libvpx )
 DEV.L. vp9                  Google VP9 (decoders: vp9 libvpx-vp9 vp9_cuvid vp9_qsv ) (encoders: libvpx-vp9 vp
9_qsv )
```

注意，要找编码器`encoder`用于编码，而非解码器`decoder`，如

```
(encoders: libx264 libx264rgb h264_amf h264_nvenc h264_qsv nvenc nvenc_h264 )
```

`nvenc`是 Nvidia 加速技术，`qsv`是 Intel 加速技术，假如选择`h264_qsv`，可以通过以下命令查看编码器详细的参数说明

```powershell
PS ffmpeg -h encoder=h264_qsv
Encoder h264_qsv [H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (Intel Quick Sync Video acceleration)]:
    General capabilities: delay hybrid
    Threading capabilities: none
    Supported pixel formats: nv12 p010le qsv
h264_qsv encoder AVOptions:
  -async_depth       <int>        E..V...... Maximum processing parallelism (from 1 to INT_MAX) (default 4)
  -avbr_accuracy     <int>        E..V...... Accuracy of the AVBR ratecontrol (from 0 to INT_MAX) (default 0)
  -avbr_convergence  <int>        E..V...... Convergence of the AVBR ratecontrol (from 0 to INT_MAX) (default 0)
  -preset            <int>        E..V...... (from 1 to 7) (default medium)
     veryfast        7            E..V......
     faster          6            E..V......
     fast            5            E..V......
     medium          4            E..V......
     slow            3            E..V......
     slower          2            E..V......
     veryslow        1            E..V......
  -rdo               <int>        E..V...... Enable rate distortion optimization (from -1 to 1) (default -1)
```

编码视频时`-vcodec`选择对应的编码器即可，如

```powershell
PS ffmpeg -i ".\input.mp4" -vcodec h264_qsv -preset 2 "output.mp4"
```



### 视频错误修正

#### 时间戳错误修正

由于可能的各种意外，视频可能会出现时间戳错误，如5分钟长的视频进度条显示有30分钟，但有效的内容只有原始的5分钟内容，这可能是因为视频在推流或转码时时间戳的写入发生错误。

可以对视频进行非二次编码的容器转换修复问题，如下面的指令，将 MP4 容器转换为 H264

```bash
$ ffmpeg -i "video.mp4" -an -vcodec copy "video_fixed.h264"
```



### 参考链接

- FFmpeg Linux 命令 在线中文手册：<http://linux.51yip.com/search/ffmpeg>
- <https://blog.csdn.net/achang21/article/details/49128785>
- <https://ffmpeg.org/ffmpeg-bitstream-filters.html#aac_005fadtstoasc>
- <https://blog.csdn.net/weiyuefei/article/details/68067944>
- 关于精确拆分：<https://blog.csdn.net/matrix_laboratory/article/details/53157383>
- 关于防止负时间戳设置的说明：<https://stackoverrun.com/cn/q/11295443>
- FFmpeg 进度寻找时容易遇到的参数位置问题：<https://trac.ffmpeg.org/wiki/Seeking#Notes>
- <https://segmentfault.com/q/1010000014772585>
- <https://blog.csdn.net/qq_39575835/article/details/83826073>
- <https://blog.csdn.net/qq_39575835/article/details/83826073>
- <https://blog.csdn.net/StimmerLove/article/details/89405064>

