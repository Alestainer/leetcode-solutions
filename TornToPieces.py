import sys

__author__ = 'alestainer'

class Solution:
    visited = set()
    dictionary = dict()
    def find_a_path(self, start, end):
        """
        :rtype
        """
        self.visited.add(start)
        if (end in self.dictionary[start]):
            return start + " " + end
        elif (self.dictionary[start] <= self.visited):
            return -1
        elif max(map(lambda x: Solution().find_a_path(start=x, end=end), list(self.dictionary[start] - self.visited))) == -1:
            return -1
        else:
            return  start + " " + max(map(lambda x: Solution().find_a_path(start=x, end=end), self.dictionary[start]))

    def __init__(self, dictionary):
        self.visited = set()
        self.dictionary = dictionary

if (__name__ == 'main.py'):
    vertexes = []
    neighbors = []
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
    for i in range(int(lines[0])):
        stations = lines[i].split(' ')
        vertexes.append(stations[0])
        neighbors.append(set(stations[1:]))
    start, end = lines[-1]
    dictionary = dict(zip(vertexes, neighbors))
    Solution(dictionary=dictionary).find_a_path(start=start, end=end)



