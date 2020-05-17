class Solution:
    def __init__(self):
        self.maxvalue = 2 ** 31 - 1
        self.minvalue = -2 ** 31

    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if len(str) == 0:
            return 0
        if str[0] != '+' and str[0] != '-' and (str[0] < '0' or str[0] > '9'):
            return 0

        ans = 0
        neg = False  # 正数
        if str[0] == '-':  # 负数
            neg = True
        i = 0
        if str[0] < '0' or str[0] > '9':  # 非数字
            i = 1

        while i < len(str) and '0' <= str[i] and str[i] <= '9':
            ans = 10 * ans + (int(str[i]))
            i = i + 1
            if (not neg and ans > self.maxvalue):  # 正数，超上限
                ans = self.maxvalue
                break

            if (neg and ans > self.maxvalue):  # 负数
                ans = -self.minvalue
                break
        if neg:
            return -ans
        else:
            return ans


s = Solution()
print(s.myAtoi("   -42"))







