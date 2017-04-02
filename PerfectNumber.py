__author__ = 'alestainer'


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num < 2):
            return False
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                sum += (num / i) + i
        return True if (num == sum) else False