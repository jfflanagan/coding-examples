max_weight  = 5

items = [4,5,3,2]
item_value_table = {
    5 : 60,
    4 : 40,
    3 : 50,
    2 : 30
}

# DP Table algorithm
table = [[0 for weight in range(max_weight + 1)] for item in range(len(items))]
for i, item_weight in enumerate(items):
    for total_weight in range(max_weight + 1):
        dont_choose = 0 if i == 0 else table[i - 1][total_weight]
        do_choose = 0 if total_weight - item_weight < 0 else table[i][total_weight - item_weight]
        do_choose += 0 if total_weight < item_weight  else item_value_table[item_weight]
        table[i][total_weight] = max(do_choose, dont_choose)

#print(table)

#Recursive algorithm
def knap_sack(total_weight, items, item_value_table, index):
    if index < 0:
        return 0

    if items[index] > total_weight:
        return 0
    
    do_choose = knap_sack(total_weight - items[index], items, item_value_table, index)
    do_choose += 0 if total_weight < items[index] else item_value_table[items[index]]
    dont_choose = knap_sack(total_weight, items, item_value_table, index - 1)

    return max(do_choose, dont_choose)

print(knap_sack(5, items, item_value_table, 3)) 
