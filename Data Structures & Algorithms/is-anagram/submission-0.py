class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = {}
        secondWord = {}

        for i in s:
            if i in firstWord:
                firstWord[i]+=1
            else:
                firstWord[i] = 1

        for j in t:
            if j in secondWord:
                secondWord[j]+=1
            else:
                secondWord[j] = 1
        
        if firstWord == secondWord:
            return True
        
        return False
