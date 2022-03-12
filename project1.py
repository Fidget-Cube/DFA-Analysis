# Author(s)
#   Max vonBlankenburg
#   Zachary Robinson

from part1 import part1
from part2 import part2

def main():
    part = input("Would you like to solve part 1, solve for part 2, or run the given test cases? (1/2/test) ")
    if part == '1':
        print("Enter an integer for the length of the string")
        length = input()

        DFACount = part1()
        print("Number of possible strings of size " + str(length) + " that map to our language: " + str(part1().count(int(length))))
    elif part == '2':
        S = input("Enter a comma-separated list of accepted one-digit inputs (e.g. 1,2,3): ")
        S = S.split(',')
        symbols = []
        for i in range(len(S)):
            if S[i] in ['0','1','2','3','4','5','6','7','8','9']:
                symbols.append(int(S[i]))
        k = int(input("Enter the modulus #: "))
        while k < 1 or k > 99999:
            k = int(input("Modulus out of range (# > 0 and # < 99999): "))
        smallest = part2()
        print(f'Smallest possible number divisible by {str(k)} given the number set {str(symbols)}: {str(smallest.FindString(symbols, k))}')
    elif part == "test":
        print("Testing part 1:")
        # Test case 1:
        length = 6
        DFACount = part1()
        answer = str(DFACount.count(int(length)))
        if answer == "1560":
            print(f" Test case 1 passed: {answer}")
        else:
            print(f" Test case 1 failed: {answer}")
        
        # Test case 2:
        length = 56
        DFACount = part1()
        answer = str(DFACount.count(int(length)))
        if answer == "1144518781838828768850216":
            print(f" Test case 2 passed: {answer}")
        else:
            print(f" Test case 2 failed: {answer}")

        print("Testing part 2:")
        # Test case 1:
        k = 26147
        symbols = [1, 3]
        smallest = part2()
        answer = str(smallest.FindString(symbols, k))
        if answer == "1113313113":
            print(f" Test case 1 passed: {answer}")
        else:
            print(f" Test case 1 failed: {answer}")

        #Test case 2:
        k = 198217
        symbols = [1]
        smallest = part2()
        theOnes = str(smallest.FindString(symbols, k))
        if  theOnes[0] == '1' and len(theOnes) == 10962 and theOnes == len(theOnes) * theOnes[0]:
            print(f" Test case 2 passed (this one would take up the entire terminal window to print)")
        else:
            print(f" Test case 2 failed")

        # Test case 3
        k = 135
        symbols = [1, 3, 7]
        smallest = part2()
        answer = str(smallest.FindString(symbols, k))
        if answer == "No solution":
            print(f" Test case 3 passed: {answer}")
        else:
            print(f" Test case 3 failed: {answer}")



if __name__ == "__main__":
    main()