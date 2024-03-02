
def get_ab(eval_stack):
    b = eval_stack.pop()
    a = eval_stack.pop()
    return a, b

def evaluate(expression):
    eval_stack = []
    for item in expression:
        if item == '+':
            a,b = get_ab(eval_stack)
            eval_stack.append(a + b)
            continue
        if item == '-':
            a,b = get_ab(eval_stack)
            eval_stack.append(a - b)
            continue
        if item == '/':
            a,b = get_ab(eval_stack)
            eval_stack.append(a / b)
            continue
        if item == '*':
            a,b = get_ab(eval_stack)
            eval_stack.append(a * b)
            continue

        eval_stack.append(item)

    return eval_stack[0]


exp = [4, 5, 7,2, '+', '-', '*']
#exp = [3 , 4, '+', 2, '*', 7, '/']

print(evaluate(exp))

