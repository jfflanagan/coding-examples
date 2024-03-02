def threeSum(nums):
    nums_sort = nums.sorted()

    


    return triplets

def twoSum(nums, target):
    diff_hash = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in diff_hash:
            return [i, diff_hash[diff]]
        else:
            diff_hash[num] = i

    return []

if __name__ == '__main__':
    print(twoSum([3,2,4], 6))