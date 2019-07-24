"""
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
"""
f = open('D:\\1.text', 'w')
i = 0
while i < 20:
    f.write('python 非常简单 \n')
    i += 1
f.close()

r = open('D:\\1.text')
# str = r.read()
# print(str)
line = r.readline()
print(line)
lines = r.readlines()
print(lines)
r.close()

aPlus = open('D:\\1.text', 'a+')
aPlus.write('Java 也不赖')
aPlus.close()