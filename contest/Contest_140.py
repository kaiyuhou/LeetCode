# class Solution:
#     def findOcurrences(self, text: str, first: str, second: str):
#         words = text.split(' ')
#         ans = []
#
#         if len(words) == 0:
#             return ans
#
#         for i in range(1, len(words) - 1):
#             if words[i - 1] == first and words[i] == second:
#                 ans.append(words[i + 1])
#
#         return ans
#
# s = Solution()
# # text = "alice is a good girl she is a good student"
# # first = "a"
# # second = "good"
# text = "we will"
# first = "we"
# second = "will"
#
# print(s.findOcurrences(text,first,second))

from contest.Tree import *

class Solution:
    def sufficientSubset(self, org_root: TreeNode, limit: int) -> TreeNode:

        def travel(root, sum):

            if root.left == None and root.right == None:
                if sum + root.val < limit:
                    return False
                else:
                    return True

            is_del = True
            if root.left:
                if travel(root.left, sum + root.val):
                    is_del = False
                else:
                    root.left = None
            if root.right:
                if travel(root.right, sum + root.val):
                    is_del = False
                else:
                    root.right = None
            return not is_del

        if travel(org_root, 0):
            return org_root
        else:
            return None
#
# s = Solution()
# root = list_to_tree([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14])
# root = list_to_tree([714,839,967,246,703,-418,455,-900,23,-583,-736,603,726,-634,384,954,-760,922,23,-357,8,-577,121,-671,-812,-385,705,-885,353,-70,42,706,218,-566,-295,-620,-699,141,104,-966,559,581,-402,None,None,677,757,-431,-807,169,262,-874,168,None,None,-401,207,-235,-23,-378,-185,-74,-864,273,602,79,-234,-385,-475,971,22,-865,-713,-814,393,68,32,-730,898,-657,572,-726,718,-640,-839,-231,852,201,339,11,516,730,-514,714,-401,7,567,-745,-422,71,-881,-836,180,-523,-411,-248,788,None,None,-400,323,915,-636,-939,-550,-336,500,-601,36,43,-872,-362,21,None,None,None,None,489,880,None,None,None,None,None,None,None,318,-342,171,-422,93,302,569,991,869,-308,674,32,699,32,-589,913,811,None,822,None,-415,-781,None,-175,None,None,-940,-670,-114,809,None,-248,-445,278,-944,None,None,659,-237,369,100,-654,-419,191,-390,-583,124,None,755,263,-775,None,50,-609,-54,-319,579,None,None,-853,-153,-775,514,853,-45,790,-53,395,861,None,-818,None,None,None,-392,253,None,862,None,375,None,-843,-538,-417,-211,810,None,85,92,None,None,-174,-717,-942,175,-641,682,None,-132,-369,-659,139,-830,-206,343,None,-330,-897,-549,-509,240,-611,None,None,None,930,-239,-950,559,729,-616,-337,350,863,-38,851,-872,None,None,-267,394,None,720,778,408,-560,304,None,None,-675,535,None,None,None,667,None,-796,-733,None,None,None,-680,138,-909,None,169,944,None,3,825,-173,-615,-720,None,115,-260,214,784,None,-485,None,18,188,870,None,-659,-232,170,715,318,6,649,None,-320,-742,None,None,None,None,657,None,763,None,-280,278,163,93,574,498,None,920,-904,-82,-427,None,-789,None,None,609,889,-736,334,-481,-603,203,None,991,None,None,None,23,-480,-537,-289,None,None,None,-932,-935,97,-526,537,-950,149,-419,None,803,-898,None,None,None,None,-843,None,-418,596,809,-824,None,None,811,180,None,794,523,781,-502,-196,-475,798,-601,-229,336,None,-628,None,-699,None,352,-616,788,613,-204,-641,902,144,-196,-199,None,None,None,-792,None,None,None,-422,None,302,584,468,499,9,-364,768,-937,271,-167,-37,None,-270,-696,-543,-245,None,622,891,-91,None,472,None,12,-659,-796,None,-290,250,-305,None,None,-881,-58,988,None,None,173,None,None,None,None,None,None,-998,-192,1000,802,333,435,-212,872,624,382,919,392,518,None,414,None,323,670,None,None,462,706,173,-304,None,None,565,-434,400,-198,None,None,-728,None,479,None,None,985,None,-221,-611,403,915,None,None,None,None,None,None,None,None,None,796,-323,None,844,None,None,None,None,None,None,None,237,None,None,-184,-273,-613,None,402,-301,None,None,None,739,568,-378,963,638,-269,-87,863,-475,-799,-950,-76,-83,None,-686,None,None,None,None,None,723,423,815,204,-752,181,-24,None,-506,None,None,None,-941,-60,None,None,None,None,None,None,None,None,840,None,None,-792,None,None,None,None,None,54,-313,None,None,None,231,97,None,-309,398,21,-87,None,-322,-711,None,903,None,-437,-95,None,-926,None,None,-415,726,None,-274,-106,-93,-774,60,-54,443,-593,302,-655,None,473,-715,-772,897,-846,None,None,-215,790,None,-997,None,561,-956,None,None,-680,-693,813,-153,510,705,-732,-14,None,None,-187,None,33,273,None,887,None,None,None,-64,-844,68,-159,-964,-332,None,-390,None,None,-675,None,None,-565,-749,-443,207,715,906,None,None,-993,259,837,-602,181,606,710,None,351,-189,-112,877,None,70,None,None,None,None,None,None,None,None,None,None,None,-548,None,430,None,90,None,652,None,None,None,None,146,507,-301,-170,None,None,None,-934,None,71,None,None,-783,None,None,None,None,466,-148,-908,768,None,None,None,None,-955,157,None,None,None,502,None,None,None,-875,None,-429,41,488,-414,None,-445,174,None,678,None,None,None,None,752,None,None,-249,None,None,None,None,None,-330,None,None,None,-553,None,None,None,893,None,None,None,129,-788,236,-414,-273,None,None,None,None,883,None,764,821,-818,-80,None,-943,-573,541,None,-993,None,578,-889,-107,345,None,556,None,None,-661,-645,997,-432,-374,-6,None,None,None,None,-984,None,None,None,None,-213,None,None,800,-45,None,None,412,None,-806,-352,None,None,-679,463,-811,None,None,None,None,None,None,None,819,-631,542,615,None,731,-538,928,None,None,282,982,-770,-991,None,None,None,-719,555,None,None,None,None,None,None,366,-884,None,-304,None,-882,None,166,None,None,None,-665,None,None,None,None,-114,-622,-134,None,None,None,None,None,None,-173,None,877,None,-346,None,-303,244,-738,222,900,-319,None,-627,None,23,None,-687,-445,530,73,None,134,784,-455,None,None,None,None,783,-377,None,None,None,None,None,212,180,-75,None,-575,-82,-447,-658,None,755,None,-676,262,71,-980,-673,None,-465,-510,None,-214,-252,16,-522,52,None,None,None,493,-420,-923,-667,None,-325,-105,-480,None,-784,-701,None,-351,None,None,None,None,None,None,None,None,None,-613,313,509,-851,728,-380,-690,None,None,547,None,None,443,-238,-280,None,954,400,None,None,None,678,None,None,None,406,None,None,None,213,389,680,None,-214,-635,603,None,118,None,-221,None,106,-916,None,None,-101,None,None,None,None,None,None,677,None,494,None,707,-847,516,-512,None,None,567,None,774,None,533,None,999,849,493,40,378,860,581,None,-192,236,None,None,None,None,-397,-68,None,None,None,None,None,None,None,None,None,None,None,745,245,651,None,None,None,None,None,None,532,None,None,-938,None,None,None,None,None,None,303,-738,-93,-844,884,-977,None,721,None,None,None,None,None,None,None,None,None,None,None,-970,None,None,315,None,None,None,760,None,None,52,-249,-243,-409,None,None,None,None,None,None,None,None,None,601,191,975,143,None,None,-53,816,-1,None,None,None,554,None,None,17,None,None,242,None,None,None,None,None,None,None,207,161,None,None,-559,-599,None,None,-459,None,-716,964,None,None,386,697,532,-890,None,-81,None,None,884,None,None,None,None,None,None,-862,-586,216,-834,None,None,None,-404,None,None,None,None,None,None,None,-62,-970,None,None,62,749,527,465,-933,-638,None,240,None,-68,None,None,None,None,439,-816,-529,-143,51,388,None,None,None,-763,None,-350,None,908,None,-428,-516,None,None,464,None,None,None,None,None,158,-813,404,None,None,-665,648,None,-17,-810,-338,None,None,None,None,-376,-37,None,-380,657,None,None,None,235,None,206,125,None,None,None,None,None,None,None,None,-400,None,-807,None,None,None,None,112,None,None,None,210,None,None,-189,-170,385,-941,None,-878,-389,531,988,435,None,None,None,None,None,-452,None,None,None,None,None,-15,-418,None,454,None,None,None,-475,-293,None,None,-520,343,-543,None,None,-856,817,None,None,None,None,225,None,None,None,None,None,None,-124,-283,None,None,None,-654,-205,713,None,-14,None,-904,None,None,-837,666,None,None,None,981,952,None,None,None,-769,None,873,None,568,329,-815,None,None,None,-639,-299,None,None,None,None,-474,None,-56,None,-895,None,None,563,None,-854,None,184,None,None,None,750,286,-671,-975,None,None,None,-355,-892,-144,-238,433,None,None,None,None,None,None,181,None,None,849,None,None,992,-630,-399,None,-802,None,None,-709,-853,-190,10,None,None,None,None,None,None,None,-404,None,None,None,-991,None,-50,None,None,None,None,347,-299,-138,978,None,None,-650,None,None,None,-127,906,None,None,None,None,None,None,None,None,None,None,-892,631,None,None,879,None,674,655,None,56,-106,None,None,None,792,322,-253,None,None,None,None,None,None,None,None,None,None,-404,None,None,None,None,None,None,None,None,None,None,None,-906,None,None,-921,616,None,None,757,None,-850,-289,None,12,None,None,None,None,None,None,None,None,None,-546,None,None,-672,None,None,None,-561,None,-713,None,None,None,None,None,None,-523,-71,None,924,None,None,None,None,352,None,None,None,-832,None,None,None,None,209,None,None,None,None,-321,770,None,None,None,None,944,None,74,239,-816,None,None,-233,555,None,None,None,None,None,None,None,None,None,899,726,None,None,None,143,129,None,764,None,-145,None,None,-55,231,None,993,None,None,None,None,None,None,None,None,-559,847,None,None,-56,299,-544,316,-11,809,None,None,None,None,None,-137,None,None,None,None,193,None,707,None,-177,None,None,-566,None,-50,None,None,438,None,None,None,None,None,-129,-288,-209,-422,-943,-771,None,-784,-570,None,-584,-774,None,None,-512,None,None,None,None,None,None,None,None,None,172,441,None,None,None,None,-285,None,None,None,138,332,None,35,None,None,None,None,None,None,-265,None,None,None,None,-458,None,None,None,None,None,None,None,None,None,None,None,976,None,None,None,967,None,-672,None,None,None,None,None,334,None,None,806,None,357,None,-574,58,None,None,None,-943,None,None,-77,None,None,380,719,519,58,-680,None,-573,None,None,None,-798,None,None,243,-767,805,803,826,-934,None,-335,624,540,None,None,-698,None,None,405,None,None,None,222,None,None,None,None,None,None,12,None,None,None,None,None,918,-821,None,None,-951,-750,799,None,None,None,None,None,None,440,None,None,-267,None,None,None,297,None,None,365,None,None,None,232,None,None,None,None,None,None,None,None,-769,449,None,None,None,245,656,None,None,None,962,-123,-301,909,959,None,None,None,None,None,None,None,None,-966,None,None,None,None,None,None,None,-307,-767,798,None,None,None,None,None,None,None,None,-638,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-314,None,None,None,167,None,None,409,None,None,None,None,None,None,None,None,None,None,None,-918,-413,36,None,482,None,-724,704,-25,390,707,None,None,None,None,-485,None,None,None,None,None,None,None,None,None,None,None,None,-121,238,460,None,None,None,188,100,274,987,544,None,None,None,-395,None,None,None,-753,None,None,None,-746,None,152,None,None,None,None,None,735,392,None,None,None,None,None,None,-790])
# limit = -2
# # limit = 1
#
# # [5, 4, 8, 11, null, 17, 4, 7, null, null, null, 5]
# print(tree_to_list(s.sufficientSubset(root, limit)))


# class Solution:
#     def smallestSubsequence(self, text: str) -> str:
#         N = len(text)
#
#         if N == 1:
#             return text
#         if N == 0:
#             return ''
#
#         # ch = max(text)
#         # for i in range(N - 1, -1, -1):
#         #     if text[i] != ch:
#         #         continue
#         #
#         #     left = self.smallestSubsequence(text[0:i].replace(ch, ''))
#         #     right = text[i + 1:].replace(ch, '')
#         #
#         #     for letter in left:
#         #         right = right.replace(letter, '')
#         #     right = self.smallestSubsequence(left)
#         #     return left + ch + right
#         letters = []
#         for t in text:
#             if t not in letters:
#                 letters.append(t)
#         letters.sort()
#         M = len(letters)
#         pos = [-1 for _ in range(M)]
#
#         def find_last(A, ch):
#             for i in range(len(A) - 1, -1, -1):
#                 if A[i] == ch:
#                     return i
#
#         pos[-1] = find_last(text, letters[-1])
#
#
#         for i in range(M - 2, -1, -1):
#             posi = N + 1
#             for j in range(i + 1, M):
#                 if letters[i] in text[:pos[j]]:
#                     posi = min(posi, find_last(text[:pos[j]], letters[i]))
#                 elif letters[i] in text[pos[j] + 1:]:
#                     posi = min(posi, find_last(text[pos[j] + 1:], letters[i]))
#             pos[i] = posi
#
#
#         ans = []
#         for i in range(N):
#             if i in pos:
#                 ans.append(text[i])
#         return ''.join(ans)
#
# s = Solution()
# A = "cdadabcc"
# # A = "abcd"
# # A = "ecbacba"
# # A = "leetcode"
# print(s.smallestSubsequence(A))















