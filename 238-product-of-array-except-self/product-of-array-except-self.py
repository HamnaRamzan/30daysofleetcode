class Solution:
    def productExceptSelf(self, nums):
        """
        Calculates the product of all elements in nums except for nums[i] for each element.

        Args:
            nums: A list of integers.

        Returns:
            A list where answer[i] is the product of all elements in nums except nums[i].
        """

        n = len(nums)
        left_product = [1] * n  # Stores the product of all elements to the left of each index
        right_product = [1] * n  # Stores the product of all elements to the right of each index

        # Calculate left product (excluding current element)
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # Calculate right product (excluding current element)
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # Combine left and right products to get the final result
        for i in range(n):
            nums[i] = left_product[i] * right_product[i]

        return nums
