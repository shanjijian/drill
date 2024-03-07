# Drill: 小转风爆破器
![MTAwMTM1XzE2NDQ1MTI1ODcwMzI=](https://github.com/shanjijian/drill/assets/42663412/bd94f7de-3e1c-44c3-85a3-0369b474e889)

纯Python实现。目前支持ssh、rdp爆破。
## 使用简介
```python
(.venv) shanjijian@shanjijiandeMacBook-Pro drill % python drill.py -h
usage: drill.py [-h] [-host HOST] [-port PORT] [-type TYPE] [-username USERNAME] [-passfile PASSFILE]

小转风爆破器

optional arguments:
  -h, --help            show this help message and exit
  -host HOST, --host HOST  主机地址
  -port PORT, --port PORT  端口
  -type TYPE, --type TYPE  爆破类型: ssh/rdp
  -username USERNAME, --username USERNAME  用户名
  -passfile PASSFILE, --passfile PASSFILE  密码字典文件

```
