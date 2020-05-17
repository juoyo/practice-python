# 考试单行多行输入输出规范示例
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))  # 1 1