class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list = {}
        for num in nums:
            if num in my_list:
                my_list[num] += 1
            else: 
                my_list[num] = 1
        sorted_items = sorted(my_list.items(), key=lambda item: item[1], reverse=True)
        top_k = sorted_items[:k]
        return[num for num,count in top_k]