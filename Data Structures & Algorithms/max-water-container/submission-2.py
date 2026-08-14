class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0
        r = len(heights) - 1
        max_so_far = 0
        while l < r:
            area = (r-l)* min(heights[l],heights[r])
            max_so_far = max(area,max_so_far)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return max_so_far
        