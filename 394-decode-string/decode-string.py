class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                current_str = ''
                while stack[-1] != '[':
                    current_str = stack.pop() + current_str
                current_num = ''
                stack.pop()
                while stack and stack[-1].isdigit():
                    current_num = stack.pop() + current_num
                current_str = int(current_num) * current_str
                stack.append(current_str)

        return ''.join(stack)