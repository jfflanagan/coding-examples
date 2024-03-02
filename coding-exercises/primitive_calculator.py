# Uses python3
import sys

def optimal_sequence(n):
    #dp_table_plus_1 = [0]
    dp_table_mult_2 = [0]
    dp_table_mult_3 = [0]

    #for i in range(1, n):
    #    dp_table_plus_1.append(i)

    for i in range(1, n):
        if (i + 1) % 2 == 0:
            m = (i + 1) // 2 - 1
            dp_table_mult_2.append(min(dp_table_mult_2[m] + 1, dp_table_mult_3[m] + 1))
        else:
            dp_table_mult_2.append(dp_table_mult_2[i - 1] + 1)

        if (i + 1) % 3 == 0:
            m = (i + 1) // 3 - 1
            dp_table_mult_3.append(min(dp_table_mult_2[m] + 1, dp_table_mult_3[m] + 1))
        else:
            dp_table_mult_3.append(dp_table_mult_3[i - 1] + 1)
    
    i = n
    sequence = []
    while i >= 1:
        sequence.append(i)
        if dp_table_mult_3[i - 1] <= dp_table_mult_2[i - 1]:
            if i % 3 == 0:
                i = i // 3
            else:
                i -= 1
        else:
            if i % 2 == 0:
                i = i // 2
            else:
                i -= 1
    
    return reversed(sequence)

def optimal_sequence_not_safe(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
