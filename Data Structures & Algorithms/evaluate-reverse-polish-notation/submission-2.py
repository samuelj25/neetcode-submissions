class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for t in tokens:
            if (t not in operators):
                stack.append(int(t))
            else:
                num_two = stack.pop()
                num_one = stack.pop()

                if (t == '+'):
                    stack.append(num_one + num_two)
                elif (t == '-'):
                    stack.append(num_one - num_two)
                elif (t == '*'):
                    stack.append(num_one * num_two)
                else:
                    stack.append(int(num_one / num_two))
        
        return stack[-1]
