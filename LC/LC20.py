class Solution:
    def isValid(self, s: str) -> bool:
        '''
        左括号，入栈
        右括号，判断是否与栈顶匹配
        最终，栈空
        '''
        symbol_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            if c == ')' or c == ']' or c == '}':
                if stack == []:
                    return False
                temp = stack.pop(-1)
                if symbol_map[temp] != c:  # 如果不匹配，返回False
                    return False
        return not stack



s = Solution()
print(s.isValid(")"))