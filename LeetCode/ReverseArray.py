#String
#Say we have an input array of s[], how do you reverse the array or string?

class Solution(object):
    def reverseString(self, s): #Do not use slicing
        index = len(s)
        stringAns = []
        for i in s:
            stringAns += s[index-1]
            index = index - 1
        #slicedString = s[::-1]
        return stringAns
    
s = ["h", "e", "l", "l", "o"]
obj = Solution()
print(obj.reverseString(s))
        

# s = "LOVE"
# stringLength = len(s)
# slicedString = s[stringLength::-1] #s[::-1]
# print(slicedString)

# s = "LOVE"
# reverseString = "" #or reverseString = []
# index = len(s)
# for x in s:
#     reverseString += s[index-1]
#     index = index - 1
# # while index > 0:
# #     reverseString += s[index-1]
# #     index = index -1
# print(reverseString)

# class Solution(object):
#     def reverseString(self, s):
#         index = len(s)
#         slicedString = s[::-1]
#         return slicedString
    
# s = ["h", "e", "l", "l", "o"]
# obj = Solution()
# obj.reverseString(s)
        