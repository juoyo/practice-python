#coding=utf-8
import sys
if __name__ == "__main__":

    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))

    # values.sort()

    for i in range(len(values)):
        temp = values[:i] + values[i+1:]
        temp.sort()
        num = temp[(0 + len(temp)) // 2]
        print(num)
    # print(values)
    # print(res)

