# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson

from queue import Queue
from sys import maxsize

class part2:
    def delta(self, p, q):
        return 10 * p + q


    def FindString(self, S, k):

        Q = Queue(maxsize = 999999)

        Q.put(0)
        while Q.qsize() > 0 and Q.qsize() < 999999:
            current = Q.get()
            for symbol in S:
                # Check if permitted digits contains only 0
                if len(S) == 1 and symbol == 0: 
                    return 'No Solution'
                # Transition states and check if its valid
                next = self.delta(current, symbol)
                if next % k == 0 and next != 0:
                    return next
                else:
                    Q.put(next)
        return 'No solution'

