class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor_arr = 0
        for i in n:
            xor_arr = xor_arr ^ n[i]
        return xor_arr

n = []
obj = Solution()