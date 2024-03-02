import re

class Solution:
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
        self.precidence = {'+':2, '-':2, '*':3, '/':3, '(':1}

    def create_postfix(self, eval_string):
        """
        Shunting yard algorithm
        """
        postfix = []
        operator_stack = []
        for op in eval_string:
            if op == ')':
                while operator_stack[-1] != '(':
                    postfix.append(operator_stack.pop())
                operator_stack.pop()
                continue

            if op == '(':
                operator_stack.append(op)
                continue              

            if op in self.operators:
                while operator_stack and self.precidence[op] <= self.precidence[operator_stack[-1]]:
                    postfix.append(operator_stack.pop())
                operator_stack.append(op)
                
            else:
                postfix.append(op)

        while operator_stack:
            postfix.append(operator_stack.pop())

        return postfix

    def eval_postfix(self, postfix):
        eval_stack = []

        for op in postfix:
            if op in self.operators:
                b = int(eval_stack.pop())
                a = 0
                if eval_stack:
                     a = int(eval_stack.pop())
                eval_stack.append(self.eval(a, b, op))
            else:
                eval_stack.append(op)

        if len(eval_stack) == 1:
            return eval_stack[0]
        else:
            return None


    def eval(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b

        # raise exception

    def calculate(self, s):
        # parse the string


        operations = re.findall('\d+|[+*/\-()]', s)
        postfix = self.create_postfix(operations)
        return self.eval_postfix(postfix)

            


s = Solution()
#postfix = s.create_postfix("2 + 3 * 4 - 1")
#print(postfix)
#print(s.eval_postfix(postfix))
#print(s.calculate("- (3 + (4 + 5))"))
print(s.calculate("(- 1 + 2)*-1"))

