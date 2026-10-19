class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        word3=[]
        while l<len(word1) and r<len(word2):
            word3.append(word1[l])
            word3.append(word2[r])
            l+=1
            r+=1
        word3.append(word1[l::])
        word3.append(word2[r::])
        return "".join(word3)

