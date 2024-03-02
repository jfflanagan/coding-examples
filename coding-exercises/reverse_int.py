def reverse_digit(x):
    reversed_digit = 0
    digit_to_reverse = x
    if x < 0:
        digit_to_reverse *= -1

    while digit_to_reverse:
        reversed_digit *= 10

        digit = digit_to_reverse % 10
        digit_to_reverse = digit_to_reverse // 10

        reversed_digit += digit

    if x < 0:
        reversed_digit *= -1

    if reversed_digit > 2147483648:
        return 0
    else:
        return reverse_digit


if __name__ == '__main__':
    print(reverse_digit(1534236469))
