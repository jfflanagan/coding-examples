import math
from collections import defaultdict
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
    hash_count = defaultdict(int)
    for num in arr:
      hash_count[num] += 1
      
    num_sums = 0
    for num in arr:
      if k - num in hash_count:
        num_sums += hash_count[k - num]
        if k - num == num:
            num_sums -= 1

        
    return num_sums // 2

print(numberOfWays([1, 2, 3, 4, 3], 6))