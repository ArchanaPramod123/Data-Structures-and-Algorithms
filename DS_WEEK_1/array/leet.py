class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=set(s)
        d=set()
        for i in a:
            d.add(s.count(i))
        if len(d)==1:
            return True
        else:
            return False
ll=Solution()
s='abc'
s1=ll.areOccurrencesEqual(s)
print(s1)
            
        