#coding=utf-8
# 3,1,4,2
# 3
a = input().split(",")
b = input().split(",")
for i in range(len(a)):
    a[i] = int(a[i])
for j in range(len(b)):
    b[j] = int(b[j])

a.sort()
b.sort()
if len(b) <= 1:
   d1 = a[-1] - b[0]
   d2 = b[0] - a[0]
   d = max(d1, d2)
   print(d)
else:
    lb = []
    for i in range(len(b) - 1):
        lb.append(int(b[i + 1]) - int(b[i]))
    d = max(lb) / 2
    if d >= int(b[0]) and d >= len(a) - int(b[-1]):
        print(d)
    else:
        d = max(b[0], len(a) - int(b[-1]))
        print(d)

    # print(2)