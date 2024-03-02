
import math

def swap(my_list, pIndex, i):
    temp = my_list[pIndex]
    my_list[pIndex] = my_list[i]
    my_list[i] = temp

# O(n) 
def moveZerosBetter(nums):
    pIndex = 0
    for i, num in enumerate(nums):
        if num == 0:
            swap(nums, pIndex, i)
            pIndex += 1

num = [1, 2,0 ,4,6,0,8, -5]

# O(n log n)
#test = sorted(num, key=lambda x : math.fabs(x), reverse=True)

moveZerosBetter(num)

def SortDigit(nums, digit):
    pIndex = 0
    for i, num in enumerate(nums):
        if num <= digit:
            swap(nums, pIndex, i)
            pIndex += 1

nums = [0,1,0,2,0,1,2,0,1]
SortDigit(nums, 0)
SortDigit(nums, 1)

print nums
