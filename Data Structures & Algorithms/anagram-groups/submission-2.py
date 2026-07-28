class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char)-ord('a')] += 1
            seen[tuple(count)].append(st)
        return list(seen.values())

        