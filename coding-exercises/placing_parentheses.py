# Uses python3

class MaxValue(object):
    def __init__(self, expression):
        self.values = []
        self.operations = []
        for i in range(len(expression)):
            if i % 2 == 0:
                self.values.append(int(expression[i]))
            else:
                self.operations.append(expression[i])

        self.M = [[0]*len(self.values) for i in range(len(self.values))]
        self.m = [[0]*len(self.values) for i in range(len(self.values))]


    def get_MinMax(self, i, j):
        min_value = float('inf')
        max_value = -float('inf')

        for k in range(i, j):
            a = self.evalt(self.M[i][k], self.M[k + 1][j], self.operations[k])
            b = self.evalt(self.M[i][k], self.m[k + 1][j], self.operations[k])
            c = self.evalt(self.m[i][k], self.M[k + 1][j], self.operations[k])
            d = self.evalt(self.m[i][k], self.m[k + 1][j], self.operations[k])

            min_value = min(min_value, a, b, c, d)
            max_value = max(max_value, a, b, c, d)

        return (min_value, max_value)

    def get_maxvalue(self):
        for i, value in enumerate(self.values):
            self.M[i][i] = value
            self.m[i][i] = value
        
        for s in range(len(self.values) - 1):
            for i in range(len(self.values) - s - 1):
                j = i + s + 1

                min_value, max_value = self.get_MinMax(i, j)
                self.M[i][j] = max_value
                self.m[i][j] = min_value

        return self.M[0][len(self.values) - 1]

    def evalt(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

def get_maximum_value(dataset):
    max_value_para = MaxValue(dataset)

    return max_value_para.get_maxvalue()


if __name__ == "__main__":
    print(get_maximum_value(input()))
