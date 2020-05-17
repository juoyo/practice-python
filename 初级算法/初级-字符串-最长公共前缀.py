class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        maxstr = strs[0]
        while maxstr:
            # print(maxstr)
            for i in range(len(strs)):
                if i == len(strs) - 1 and strs[-1].find(maxstr) == 0:
                    return maxstr
                if strs[i].find(maxstr) == 0:
                    continue
                else:
                    maxstr = maxstr[0: -1]
                    break
        return maxstr


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))



