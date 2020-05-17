def main():
    n = int(input())
    ls = []
    for i in range(n):
        ls.append(input())
    ls.sort()
    for i in ls:
        print(i)


if __name__ == '__main__':
    main()