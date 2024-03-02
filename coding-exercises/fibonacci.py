def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# DP example
def fibonacci_dp(number):
    if number < 2: # also check for int type
        return number

    table = [0]*(number + 1)
    for i in range(0, number + 1):
        if i < 2:
            table[i] = i
            continue
    
        table[i] += table[i - 1] + table[i - 2]
    return table[ -1]

print fibonacci_dp(7)