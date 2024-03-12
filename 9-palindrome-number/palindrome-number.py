class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev=0
        while temp>0 :
            unit=temp%10
            rev=rev*10 + unit
            temp=temp/10

        if rev == x:
            return True
        else:
            return False

        