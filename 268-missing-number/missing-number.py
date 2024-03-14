class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor1=0
        xor2=0
        for i in range(0,len(nums)):
            xor2=xor2^nums[i]
            print(xor2)
            xor1=xor1^(i)
            print(xor1)
            
        xor1= xor1^(len(nums))
        print(xor1)

        return xor1^ xor2


        