__author__ = 'alestainer'

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dups = set(nums)
        if (len(no_dups) == 1):
            return no_dups.pop()
        if (len(no_dups) == 2):
            x = no_dups.pop()
            y = no_dups.pop()
            return x if (x > y) else y
        three_max = []
        for i in range(3):
            three_max.append(no_dups.pop())
        three_max.sort()
        unique = len(no_dups)
        for i in range(unique):
            candidate = no_dups.pop()
            for j in range(3):
                if (candidate > three_max[0] and candidate < three_max[1]):
                    three_max[0] = candidate
                if (candidate > three_max[1] and candidate < three_max[2]):
                    three_max[0] = three_max[1]
                    three_max[1] = candidate
                if (candidate > three_max[2]):
                    three_max[0] = three_max[1]
                    three_max[1] = three_max[2]
                    three_max[2] = candidate
        return three_max[0]
