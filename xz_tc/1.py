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

    print(n, line1, m, line2)

    res = [[]]

    for i in range(len(line1)):
        for j in range(len(line2)):
            if i == 0 or j == 0:
                res[i][j] = 0
            else:
                if line1[i] == line2[j]:
                    res[i][j] = 