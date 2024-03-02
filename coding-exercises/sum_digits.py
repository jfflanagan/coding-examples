def sum_digits(num):
    summ = 0
    while num > 0:
        digit = num % 10
        num //= 10

        temp = (digit + summ)
        summ = temp % 10
        if temp > 9:
            summ += 1

    return summ

print(sum_digits(88888888))



