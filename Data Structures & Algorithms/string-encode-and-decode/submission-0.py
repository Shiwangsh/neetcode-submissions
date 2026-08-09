class Solution:

    def encode(self, strs: List[str]) -> str:
        my_str = []
        for char in strs:
            char = str(len(char))+'#'+char
            my_str.append(char)
        return("".join(my_str))
        

    def decode(self, s: str) -> List[str]:
        # 2#ab1#c
        my_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            my_list.append(word)
            i = j + 1 + length
        return my_list


