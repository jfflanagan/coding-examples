
def summ(current_sum, depth, count):
    if current_sum == 9:
        return count + 1

    if depth > 4 or current_sum > 9:
        return count

    for i in range(10):
        current_sum += i
        count = summ(current_sum, depth + 1, count)
        current_sum -= i

    return count

print(summ(0, 1, 0))