class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        myList = []
        i = 0
        while i < n:
            i = i+1 
            myList.append(str(i))
        myList = sorted(myList)
        return myList
