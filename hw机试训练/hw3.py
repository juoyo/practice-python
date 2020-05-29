#coding=utf-8
n = int(input())  # 书的本数
r = int(input())  # 人数
b = []
count = 0
for i in range(r):  # 每个人喜欢的书的列表
    b.append(input().split())
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])
for j in range(len(b) - 1):
    for i in range(len(b) - 1):
        if b[i][-1] > b[i + 1][-1]:
            b[i], b[i + 1] = b[i + 1], b[i]
end = -1
for i in range(r):
    if end >= b[i][0] and end <= b[i].right:
        continue
    else:
        count = count + 1
        end = b[i][-1]

print(count)