import sys
for line in sys.stdin:
    s = line.strip()
    if s == "":
        pass
    if len(s) % 8 != 0:  # 如果s长度不为8的整数倍，补全为8的整数倍
        s = s + '0' * (8 - len(s) % 8)
    for i in range(0, len(s) // 8):
        print(s[0 + 8 * i : 8 + 8 * i])