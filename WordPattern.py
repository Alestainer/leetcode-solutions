__author__ = 'alestainer'


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if (len(words) != len(pattern)):
            return False
        mapping = dict()
        reversed_mapping = dict()
        mapping.update([pattern[0], words[0]])
        reversed_mapping.update(words[0], pattern[0])
        for i in range(1, len(words)):
            if (mapping.has_key(pattern[i])):
                if reversed_mapping.has_key(words[i]):

