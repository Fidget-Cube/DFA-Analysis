# Author(s)

from queue import Queue
import queue
from sys import maxsize

class part2:
    def delta(p, q, r):
        return (10 * p + q) % r


    def FindString(DFA, S, k):

        Q = queue(maxsize = 99999)
        visited = []
        parent = []
        
        for i in range(0, k-1):
            visited[i] = 0
        for i in range(0, k-1):
            parent[i] = -1

        

