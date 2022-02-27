# Author(s)

from queue import Queue
from sys import maxsize

class part2:
    def delta(self, p, q):
        return 10 * p + q


    def FindString(self, S, k):

        Q = Queue(maxsize = 99999)

        Q.put(0)
        while Q.qsize() > 0 and Q.qsize() < 99999:
            current = Q.get()
            for symbol in S:
                next = self.delta(current, symbol)
                if next % k == 0:
                    return next
                else:
                    Q.put(next)
        return 'No solution'
