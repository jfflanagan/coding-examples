def sub_arrays(input):
    stack = []
    dp_table = [1] * len(input)
    for i in range(len(input)):
        while stack and input[stack[-1]] < input[i]:
            dp_table[i] += dp_table[stack.pop()]
        stack.append(i)

    stack = []
    dp_table_b = [1] * len(input)
    for i in range(len(input) - 1, 0, -1):
        while stack and input[stack[-1]] < input[i]:
            dp_table_b[i] += dp_table_b[stack.pop()]
        stack.append(i)
        dp_table[i] += dp_table_b[i] - 1

    return dp_table 


a = [2, 4, 7, 1, 5, 3]
print(sub_arrays(a))