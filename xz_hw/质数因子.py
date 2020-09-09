n = int(input())
while n != 1:
    for i in range(2, n + 1):
        while n % i == 0:  # n 可被 i 整除，i 是因子
            print(i, end = " ")
            n = n // i



