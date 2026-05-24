class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operators = ['+', '-', '*', '/']
        i = 0

        while i < len(tokens):
            if (tokens[i] not in operators):
                res.append(int(tokens[i]))
            else:
                num_two = res.pop()
                num_one = res.pop()

                if (tokens[i] == '+'):
                    temp = num_one + num_two
                    res.append(temp)
                elif (tokens[i] == '-'):
                    temp = num_one - num_two
                    res.append(temp)
                elif (tokens[i] == '*'):
                    temp = num_one * num_two
                    res.append(temp)
                else:
                    temp = int(num_one / num_two)
                    res.append(temp)
            i += 1
        
        return (res[-1])