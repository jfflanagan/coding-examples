
class SubExpression(object):
    def __init__(self, value, exp_type):
        self.value = value
        self.exp_type = exp_type

    def get_total_value(self):
        expres = ""


def get_ab(eval_stack):
    b = eval_stack.pop()
    a = eval_stack.pop()
    return a, b

def put_para(eval_string, a_type):
    if a_type == 'addsub':
        return '({0})'.format(eval_string)

    return eval_string


def to_infix(postfix):
    eval_stack = []
    for item in postfix:
        if item == '+':
            a,b = get_ab(eval_stack)
            eval_stack.append(SubExpression('{0} + {1}'.format(a.value,b.value), 'addsub'))
            continue
        if item == '-':
            a,b = get_ab(eval_stack)
            eval_stack.append(SubExpression('{0} - {1}'.format(
                a.value,
                put_para(b.value, b.exp_type)
                ), 'addsub'))
            continue
        if item == '/':
            a,b = get_ab(eval_stack)
            eval_stack.append(SubExpression('{0} / {1}'.format(
                put_para(a.value, a.exp_type),
                put_para(b.value, b.exp_type)), 'multdiv'))
            continue
        if item == '*':
            a,b = get_ab(eval_stack)
            eval_stack.append(SubExpression('{0} * {1}'.format(
                put_para(a.value, a.exp_type),
                put_para(b.value, b.exp_type)), 'muldiv'))
            continue
        eval_stack.append(SubExpression(item, 'digit'))

    return eval_stack[0] 


#exp = [3 , 4, '+', 2, '*', 7, '/']
exp = [4, 5, 7,2, '+', '-', '*']
print(to_infix(exp).value)