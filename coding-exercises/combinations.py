results = []

def subsets(nums, s, n, my_set):
    if n == 0:
        return

    if my_set:
        results.append(my_set)

    for i in range(s, n):
        subsets(nums, i + 1, n, my_set + [nums[i]])

def combinations(n, k, combo):
    if len(combo) == k:
        results.append(combo)
        return

    for num in range(1, n + 1):
        combinations(num - 1, k, combo + [num])

#combinations(4,2,[])
subsets([1,2,3], 0, 3, [])
print(results)