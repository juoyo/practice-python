n = int(input())
dic = {}
for i in range(0, n):
    index, value = input().split()
    index = int(index)
    value = int(value)
    if index not in dic:
        dic[index] = value
    else:
        dic[index] = dic[index] + value
sorted(dic)
for key in dic:
    print(key, dic[key])