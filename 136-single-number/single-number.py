class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Use bitwise XOR to find the single element
    result = 0
    for num in nums:
      result ^= num

    return result


nums = [2, 2, 3]
solution = Solution()
print(solution.singleNumber(nums)) 