s = input()
ls = []
for i in range(len(s) - 1, -1, -1):
    if s[i] not in ls:
        ls.append(s[i])

res = ""
for i in ls:
    res = res + i
print(res)


