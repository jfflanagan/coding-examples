def sort_colors(nums):
    n = len(nums)

    j = 0
    for i in range(n):
        if nums[i] < 1:
            #swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1

    j = 0
    for i in range(n):
        if nums[i] < 2:
            #swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1

def sort_colors_onepass(nums):
    n = len(nums)

    # three way partition
    i = 0
    j = 0
    k = n - 1
    while i <= k:
        if nums[i] < 1:
            #swap
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
            i += 1
        elif nums[i] > 1:
            temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
            k -= 1
        else:
            i += 1          




nums = [2,0,2,1,1,0]
#nums= [2,0, 1]
nums = [1]
sort_colors_onepass(nums)
print(nums)


    

