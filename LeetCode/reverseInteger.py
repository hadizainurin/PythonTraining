# #There are three ways to solve these which are recursion (if), while loop and slicing
#While loop
class Solution(object):
    def reverse(self, x):
        #To solve issues if we considered cases where zeroes is leading then convert number to string
        reverse = 0 #initial reverse
        while(x>0):
                key = x %10 #This is assuming that that x last number is not 0 otherwise it will return an error
                reverse = (reverse *10) + key
                x = x //10
        return reverse

#recursion
# class Solution(object):
#     def reverse(self, x):
#         revr_int 
#         if (x > 0):  
#             Reminder = x % 10  
#             revr_int = (revr_int * 10) + Reminder  
#             x = x // 10  
#         return revr_int  

#Solve using slicing method
# class Solution(object):
#     def reverse(self, x):
#         x = str(x)
#         if x[0] == '-':
#             a = int('-1' + x[-1:0:-1])
#             if a == 0:
#                 return 0
#             else:
#                 return a
#         else:
#             reverseInt = x[::-1]
#             if reverseInt == 0:
#                 return 0
#             else:
#                 return reverseInt

# #This solve issues related to leading zeroes and negative numbers
# class Solution(object):
#     def reverse(self, x):
#         rev_num = 0
#         base_pos = 1
#         if(x > 0):
#                 x = int(x / 10)
#                 rev_num += (x % 10) * base_pos
#                 base_pos *= 10
#         return rev_num

#NOTED Leetcode still considered the number as int, more efficient method needed
# class Solution(object):
#     def reverse(self, x):
#         if x > 0 and x <= 2147483647: 
#             return str(x)[::-1]
#         elif x < 0 and x >= -2147483647:
#             return '-{val}'.format(val = str(x)[1:][::-1])
#         else:
#             return 0

# class Solution(object):
#     def reverse(self, x):
#         reversedNumber=0
#         if x>0: 
#             while x>0: 
#                 reversedNumber = reversedNumber * 10 + x % 10 
#                 x //= 10 
#             if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:     
#                 return 0 
#             else: 
#                 return reversedNumber 
#         elif x==0: 
#             return 0 
#         elif x<0: 
#             x = abs(x) 
#             while x>0: 
#                 reversedNumber = reversedNumber * 10 + x % 10 
#                 x //= 10 
#             if reversedNumber >= 2 ** 31 - 1 or reversedNumber <= -2 ** 31:      
#                 return 0 
#             else: 
#                 return -reversedNumber

x = 1002
obj = Solution()
print(obj.reverse(x))
