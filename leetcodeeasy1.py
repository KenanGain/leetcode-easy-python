class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False

sol = Solution()
arr1 = [2, 6, 4, 1]
arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
print(sol.threeConsecutiveOdds(arr1))  # Output: False
print(sol.threeConsecutiveOdds(arr2))  # Output: True