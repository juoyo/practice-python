#coding=utf-8
# 3,1,4,2
# 3
a = input().split(",")  # 公交车站
b = input().split(",")  # 路灯位置
for i in range(len(a)):
    a[i] = int(a[i])
for j in range(len(b)):
    b[j] = int(b[j])

a.sort()
b.sort()
if len(b) <= 1:  # 只有一个路灯
   d1 = a[-1] - b[0]  # 最后一个公交站和路灯的距离
   d2 = b[0] - a[0]  # 第一个公交站和路灯的距离
   d = max(d1, d2)
   print(d)
else:
    lb = []
    for i in range(len(b) - 1):  # 相邻两路灯之间的距离列表
        lb.append(int(b[i + 1]) - int(b[i]))
    d = max(lb) // 2 + 1  # 路灯单侧最大照明距离

    if d >= b[0] - 0 and d >= len(a) - b[-1]:
        print(d)
    else:
        d = max(b[0] - 0, len(a) - b[-1])
        print(d)

    # print(2)