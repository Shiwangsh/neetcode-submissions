class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num - 1 in nums_set:
                continue  # not a sequence start, skip it
            
            # this IS a sequence start — now walk forward
            current_num = num
            current_length = 1
            while(current_num + 1 in nums_set):
                current_num +=1
                current_length +=1
            if current_length > longest:
                longest = current_length
            
            # your turn: while (current_num + 1) is in nums_set,
            # increment current_num and current_length
            
            # then compare current_length to longest and update longest
        
        return longest