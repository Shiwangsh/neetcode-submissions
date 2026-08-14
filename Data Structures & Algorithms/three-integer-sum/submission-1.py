class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_set = []
        length= len(nums)
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            l = i+1
            r = length -1
            while l < r:
                if (nums[l] + nums[r] > target):
                    r -= 1
                elif (nums[l] + nums[r] < target):
                    l+= 1
                else:
                    my_set.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return my_set


# nums = [-1,0,1,2,-1,-4]
# sorted = [-4,-1,-1,0,1,2]   

# i = -4 = 4 i = -1 = 1
# -1+2 = 1x [-1,-1,2]v
# -1+2 = 1x [-1,-1,2]v
# 0+2 = 2x 
# 1+2 = 3x

        