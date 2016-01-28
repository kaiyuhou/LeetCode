# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 09:42:06 2016

@author: Mike
"""

class Solution(object):
 def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mydict = dict()
    results = []
    for item in strs:
        item_ele = tuple(sorted(item))
        if not item_ele in mydict:
            mydict[item_ele] = [item]
        else:
            mydict[item_ele].append(item)
    for key in mydict:
        item_array = mydict[key]
        item_array.sort()
        results.append(item_array)
    return results
    
sln = Solution()
print sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])