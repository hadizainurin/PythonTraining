# class Solution(object):
#     def twoSum(self, nums, target):
#         index = len(nums)
#         for i in range(index):
#             for j in range (i+1, index):
#                 if nums[i] + nums[j] == target:
#                     return i,j 
# #LeetCode answer, to see its print()

#BinarySearch

# def binary_search()
#HashTable
class Solution(object):
    def twoSum(self, nums, target):
        hashTable = dict()
        try:
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashTable:
                    return (hashTable[complement],i)
                else:
                    hashTable[nums[i]] = i #Still some bug here, need to diagnose further
        except:
            print("Nothing is print")

# input = [2,7,11,15]
# output = 9
# index = len(input)
# obj = Solution()
# print(obj.twoSum(input,output))

input = [2,7,11,15]
output = 22
obj = Solution()
print(obj.twoSum(input,output))
