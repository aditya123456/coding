class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # Store the current length as the start index
                # for future reversal
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # Reverse the substring between the matching parentheses
                result[start:] = result[start:][::-1]
            else:
                # Append non-parenthesis characters to the processed list
                result.append(current_char)
        return "".join(result)


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                # Collect characters until we find the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' from the stack
                if stack:
                    stack.pop()
                # Add the collected characters back to the stack in reverse order
                stack.extend(temp)
            else:
                stack.append(char)

        return ''.join(stack)