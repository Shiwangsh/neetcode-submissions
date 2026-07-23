class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = set()
        for num in nums:
            if num in my_map:
                return True
            else:
                my_map.add(num)
        return False

        