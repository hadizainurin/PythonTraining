class Solution(object):
    def threeSum(self, nums):
        tripleArray = []
        index = len(nums)
        for i in range(index):
            for j in range (index+1,index):
                for k in range (index+1,index):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return tripleArray(nums[i],nums[j],nums[k])
           
# input = [-1,0,1,2,-1,4]
# i = 0
# while i < len(input) :
#     if input[i] + input[i+1] + input[i+2] == 0:
#         print(input[i], end =" ")
#         i += 1
#         print(input)

nums = [-1,0,1,2,-1,4]
obj = Solution()
print(obj.threeSum(nums))
