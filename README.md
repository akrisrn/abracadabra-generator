# Abracadabra Generator
不明觉厉的咒语生成器。

## 需求
- python3
  - PyMySQL
- mysql

## 用法
- 在`analyse.py`和`gen.py`中填入数据库相关信息
- `python3 analyse.py`分析`z4.txt`词汇表以获得音节数据
- `python3 gen.py`开始随机生成一句不明觉厉毫无意义乱七八糟的咒语
- 支持命令行参数
  - 参数1设定一个单词中音节的数量，默认3
  - 参数2设定一句咒语中单词的数量，默认10
  - 参数3设定随机数种子，默认无

## 栗子
```
$ python3 gen.py
ellowntti ingmeltnhab shiecvor oncdardi pyertor rgiernags tiriork morighsen itirkerc inartsorr.
$ python3 gen.py 2
bandfa mberppe caverd lderir spitce panas structske entatt nquring turngnat.
$ python3 gen.py 2 4
culspher bunsa suar onme.
$ python3 gen.py 2 4 seed
rpidev condpalm edsib mola.
```
