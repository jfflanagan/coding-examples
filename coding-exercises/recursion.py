
import Queue

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(4))

#DP example

number = 4

def factorial(number):
    if number <= 1:
        return 1

    table = [0]*number

    for i in range(0, number):
        if i == 0:
            table[i] = 1
            continue

        table[i] = (i + 1) * table[i - 1]

    return table[-1]

print factorial(4)