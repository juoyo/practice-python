#coding=utf-8
import sys
if __name__ == "__main__":
    res = []

    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line1 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values1 = list(map(int, line1.split()))

    # 读取第二行的n
    m = int(sys.stdin.readline().strip())
    line2 = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values2 = list(map(int, line2.split()))

    # print(n, type(line1), line1, m, line2)

    if values1[0] < values2[-1] or values1[-1] > values2[0] or not set(values1) & set(values2):
        print()

    hash_map = {}
    res = []
    last = 0
    if values1[0] == values2[0]:
        res.append(values2[0])
    for i in range(len(values1)):
        for j in range(len(values2)):

            if values2[j] not in values1[last + 1:]:
                continue
            else:
                last = values1.index(values2[j])
                res.append(values2[j])
    for i in range(len(res)):
        print(res[i], end=" ")