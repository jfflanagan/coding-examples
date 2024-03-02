my_list = []

def well_placed(num_open, num_closed, num, current_item):
    if num_open < num:
        well_placed(num_open + 1, num_closed, num, current_item + "(")

    if (num_open - num_closed) > 0 and num_closed < num:

        well_placed(num_open, num_closed + 1, num, current_item + ")")

    if num_open == num_closed and num_open == num:
        my_list.append(current_item) 

well_placed(0, 0, 1, "")
print(my_list)
    