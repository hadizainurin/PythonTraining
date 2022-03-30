# class Solution(object):
#     def arrayStringsAreEqual(self, word1, word2):
#         s1 = []
#         s2 = []
#         for i in word1:
#             s1 += i
#         for j in word2:
#             s2 += j
#         if (s1 == s2):
#             return True
#         else:
#             return False

#The best solution
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 =''.join(word1)
        str2=''.join(word2)
        if(str1==str2):
            return True
        return False

word1 = ["ab", "c"]
word2 = ["a", "bc"]
obj = Solution()
print(obj.arrayStringsAreEqual(word1,word2))
