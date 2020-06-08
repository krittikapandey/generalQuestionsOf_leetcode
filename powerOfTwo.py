class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n==1:
            return True
        if n==0:
            return False
        
        if n>1:
            result_str=bin(n & (n-1))
            if result_str=='0b0':
                return True
            else:
                return False
        else:
            return False
        