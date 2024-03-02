import copy

results = set()

def combo_sum(nums, current_sum, target, sum_stack, index, n):
    if current_sum == target:
        results.add(tuple(sum_stack))
        return

    for i in range(index, n):
        # stop, cannot achive result
        if target - current_sum < nums[i]:
            break

        # push canidate
        sum_stack.append(nums[i])

        index += 1
        combo_sum(nums, current_sum + nums[i], target, sum_stack, index, n)
        

        # back track
        sum_stack.pop()


nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
nums.sort()
my_stack = []

combo_sum(nums, 0, 27, my_stack, 0, len(nums))

print(results)