class Solution(object):
    from collections import Counter
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rL = Counter(ransomNote)
        mL = Counter(magazine)

        for x in rL: 
            if rL[x]>mL[x]:
                return False

        return True
