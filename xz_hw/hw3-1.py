# condeing: utf-8
n = int(input())  # 书的本数
r = int(input())  # 人数
b = []
count = 0
for i in range(r):  # 每个人喜欢的书的列表
    b.append(input().split())
print(b)

dic = {}
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] not in dic:
            dic[b[i][j]] = 1
        else:
            dic[b[i][j]] = dic[b[i][j]] + 1
print(dic)
dic_order = sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(dic_order)

res = []
visited = [0 for i in range(len(b))]
for d_o in dic_order:
    tempmax = d_o[0]  # 最大需求的书的类型
    for i in range(len(b)):
        if tempmax in b[i]:
            if visited[i] == 0:  # 这本书第一次满足b[i]
                visited[i] = 1
                if tempmax not in res:
                    res.append(tempmax)
    if 0 not in visited:  # 所有需求列表均访问，以前访问的书即为最小满足的书目
        # res.pop(-1)
        break
print(res)

print("----------------")


