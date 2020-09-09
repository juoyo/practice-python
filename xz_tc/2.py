#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, m = sys.stdin.readline().strip().split()
    n = int(n)
    m = int(m)

    # print(type(n), n, m)

    values = []
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = list(map(int, line.split()))

        values.append(value)
    zero = 0
    for value in values:
        if 0 in value:
            zero = 1
    if zero == 0:
        print(0)

    s = set()
    temp = []
    count = 0
    for value in values:
        if 0 in value:
            for v in value:
               if v != 0:
                   temp.append(v)
            count = count + len(temp)
        for t in temp:
            if t in value:
                temp.extend(value)
                break
    s = set(temp)
    print(len(s))



