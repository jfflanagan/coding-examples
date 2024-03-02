def decode(digits):
    #dp_table = [1,2]
    dp_table = []
    if int(digits[0]) > 0:
        dp_table.append(1) # dummy 
        dp_table.append(1)
    else:
        return 0

    for i in range(1, len(digits)):
        #dp_table.append(0)
        single_digit = int(digits[i])
        if single_digit > 0:
            dp_table.append(dp_table[i])
        else:
            dp_table.append(0)

        double_digit = int(digits[i-1] + digits[i])

        if double_digit > 9 and double_digit <= 26:
            dp_table[-1] += dp_table[i-1]

    return dp_table[-1]


#def decode(digits, start, end, summ):
#    if start > end:
#        return int(summ > 0)
    
#    combinations = decode(digits, start + 1, end, summ + int(digits[start]))
    
#    if start < end:
#         test_digit = int(digits[start] + digits[start + 1])
#         if test_digit <= 26 and test_digit > 9:
#             combinations += decode(digits, start + 2, end, summ + test_digit)

#    return combinations



digits = "30111"
#print(decode(digits,0,len(digits)-1, 0))
print(decode(digits))
