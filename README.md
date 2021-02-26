# 将Amazon Transcribe生成的json格式转换为srt格式

## 使用方法
```
usage: amazon-transcribe-json2srt.py [-h] [--space] JSONFILE

convert Amazon Transcribe JSON file to SRT subtitle file.

positional arguments:
  JSONFILE    Amazon Transcribe JSON file

optional arguments:
  -h, --help  show this help message and exit
  --space     space between words
```
英文要加--space参数，中文不要加，会生成一个JSONFILE.srt的文件。

## 说明
核心代码从这里抄的
https://aws.amazon.com/cn/blogs/china/adding-chinese-subtitle-with-amazon-transcribe/

转换过程简单粗暴，4秒合并为一段，没有人性地分句。上一句话末尾的标点都有可能放在一段字幕的开头。

例如：

```
1
0:0:0,40 --> 0:0:4,4260
at the southern tip of Patagonia stands a legendary mountain range

2
0:0:4,269 --> 0:0:8,4500
.If you're a climber, you can't help but be drawn to these mountains. Elite climbers Tommy

3
0:0:8,500 --> 0:0:13,5260
Caldwell has a dream to climb all seven peaks in one go 12,000

4
0:0:13,259 --> 0:0:17,4449
ft of vertical climbing. It's pretty dangerous stuff on his quest. Tommy's

5
0:0:17,449 --> 0:0:21,4469
enlisted Alex Honnold, who's famous for his boldness on the rock. He's got

6
0:0:21,480 --> 0:0:26,5020
this ability to control fear, but in the snow and ice of the high mountains

7
0:0:26,30 --> 0:0:30,4170
,Alex is a newcomer. Oh, God, can Alex and Tommy

8
0:0:30,170 --> 0:0:34,4350
overcome their rookie mistakes? Alex brought the wrong kind of cramp, wouldn't

9
0:0:34,350 --> 0:0:38,4450
know the difference and make history on the Fitz Traverse way outside my comfort zone

10
0:0:38,460 --> 0:0:42,4549
.We'll intimidated. Careful. Whoa, no

11
0:0:47,439 --> 0:0:48,1060
worse. .
```
