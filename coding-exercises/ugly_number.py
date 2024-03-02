def get_ugly_numers(n):
    ugly_numbers = [1]

    twos_i = 0
    threes_i = 0
    fives_i = 0 

    for i in range(1, n):
        twos = ugly_numbers[twos_i] * 2
        threes =  ugly_numbers[threes_i] * 3
        fives = ugly_numbers[fives_i] * 5

        next_ugly = min(twos, threes, fives)

        if next_ugly > ugly_numbers[-1]:
            ugly_numbers.append(next_ugly)

            if next_ugly == twos:
                twos_i += 1
            if next_ugly == threes:
                threes_i += 1
            if next_ugly == fives:
                fives_i += 1

        


    return ugly_numbers

print(get_ugly_numers(10))




