import math

def sumThreeJ(nums):
    n = len(nums)
    nums.sort()
    triplets = set()

    for i in range(n - 2):
        l = i + 1
        r = n - 1

        while l < r:
            summ = nums[i] + nums[l] + nums[r]

            if summ < 0:
                 l += 1
            elif summ > 0:
                r -= 1
            else:
                triplet = (nums[i], nums[l], nums[r])

                if triplet not in triplets:
                    triplets.add(triplet)

                l += 1
                r -= 1

    return triplets


def sumThreeClosest(nums, target):
    n = len(nums)
    nums.sort()

    best_sum = 10000000

    for i in range(n - 2):
        l = i + 1
        r = n - 1

        while l < r:
            summ = nums[i] + nums[l] + nums[r]

            if math.fabs(target - summ) < math.fabs(best_sum - target):
                best_sum = summ



            if summ < target:
                 l += 1
            elif summ > target:
                r -= 1
            else:
                return target

    return best_sum

print(sumThreeClosest([-1,2,1,-4], 1))








        
