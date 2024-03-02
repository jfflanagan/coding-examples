class Solution:
    def __init__(self):
        self.results = []
        
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def x(self, nums, idx, n):
        if idx == n - 1:
            self.results.append(nums[:])
            return
            
        for i in range(idx, n):
            if idx == i or nums[i] != nums[idx]:
                self.swap(nums, idx, i)
                self.x(nums, idx + 1, n)
                self.swap(nums, i, idx)
            
        
    def permute(self, nums):
        self.results = []
        
        self.x(nums, 0, len(nums))
        
        return self.results

nums = [1,1,2]
s = Solution()
r = s.permute(nums)
print(r)
