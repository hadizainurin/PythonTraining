class Solution(object):
    def addTwoNumbers(self, l1, l2):
        for i in range(len(l1)):
            for j in range(len(l2)):
                sum = l1[i] + l2[j]
        return sum
        
l1 = [2,4,3]
l2 = [5,6,4]
obj = Solution()
print(obj.addTwoNumbers(l1,l2))