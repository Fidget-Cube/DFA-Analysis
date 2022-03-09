# Author(s)
#   Max vonBlankenburg

# For purposes of clarity
# 00 = 'a'
# 01 = 'b'
# 10 = 'c'
# 11 = 'd'
class part1:
    prev = [] # Number of valid strings already determined
    next = [] # Number of valid strings being determined
    mappings = [] # All the existing state mappings that don't lead to the trap state

    def __init__(self):
        for i in range(1024): # Initialize 4^5 possible states (for all possible strings of length 5)
            self.prev.append(1)
            self.next.append(0)
            self.mappings.append(self.initializeMappings(i))
    
    # Count the number of possible strings of length n accepted by the given language
    def count(self, n):
        if n < 6:
            return 4**n
        # Loop for each length, starting at length 6
        for i in range(n - 5):
            runningTotal = 0
            # Clear 'next'
            for init in range(1024):
                self.next[init] = 0
            # Loop for each state
            for j in range(1024):
                for k in self.mappings[j]:
                    self.next[j] += self.prev[k]
                runningTotal += self.next[j]
            self.prev = self.next[:]
        return runningTotal
    
    # Perfom the function of a DFA, initializing mappings to valid end states for every 5-character state
    def initializeMappings(self, state):
        endPoints = []
        # Delta(state, 00)
        if self.isEndState(state + (0 * 4**5)):
            endPoints.append((state + (0 * 4**5)) >> 2)
        # Delta(state, 01)
        if self.isEndState(state + (1 * 4**5)):
            endPoints.append((state + (1 * 4**5)) >> 2)
        # Delta(state, 10)
        if self.isEndState(state + (2 * 4**5)):
            endPoints.append((state + (2 * 4**5)) >> 2)
        # Delta(state, 11)
        if self.isEndState(state + (3 * 4**5)):
            endPoints.append((state + (3 * 4**5)) >> 2)
        return endPoints
    
    # Determine if 'state' is a valid end state
    def isEndState(self, state):
        stateString = self.translate(state)
        if 'a' in stateString and 'b' in stateString and 'c' in stateString and 'd' in stateString:
            return True
        return False

    # Translate the state's numerical value into its representative language string
    def translate(self, state):
        stateString = ''
        for i in range(6): # assume we always test strings of length 6
            if state == 0:
                state >>= 1
                if state == 0:
                    stateString += 'a' # 00
                else:
                    stateString += 'c' # 10
            else:
                state >>= 1
                if state == 0:
                    stateString += 'b' # 01
                else:
                    stateString += 'd' # 11
            state >>= 1
        return stateString
