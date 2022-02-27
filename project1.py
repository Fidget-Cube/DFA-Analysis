from part1 import part1
from part2 import part2

def main():
    part = input("Would you like to solve part 1 or 2? (1/2) ")
    if part == '1':
        print("Enter an integer for the length of the string")
        length = input()

        DFACount = part1()
        print("Number of possible strings of size " + str(length) + " that map to our language: " + str(DFACount.count(int(length))))
    elif part == '2':
        S = input("Enter a comma-separated list of accepted one-digit inputs (e.g. 1,2,3): ")
        S = S.split(',')
        symbols = []
        for i in range(len(S)):
            if S[i] in ['0','1','2','3','4','5','6','7','8','9']:
                symbols.append(int(S[i]))
        k = int(input("Enter the modulus #: "))
        smallest = part2()
        print(f'Smallest possible number divisible by {str(k)} given the number set {str(symbols)}: {str(smallest.FindString(symbols, k))}')
    elif part == "test":
        print("Testing part 1:")
        # Test case 1:
        length = 6
        DFACount = part1()
        if str(DFACount.count(int(length))) == "1560":
            print(" Test case 1 passed")
        else:
            print(" Test case 1 failed")
        
        # Test case 2:
        length = 56
        DFACount = part1()
        if str(DFACount.count(int(length))) == "1144518781838828768850216":
            print(" Test case 2 passed")
        else:
            print(" Test case 2 failed")

        print("Testing part 2:")
        # Test case 1:
        k = 26147
        symbols = [1, 3]
        smallest = part2()
        if str(smallest.FindString(symbols, k)) == "1113313113":
            print(" Test case 1 passed")
        else:
            print(" Test case 1 failed")

        #Test case 2:
        k = 198217
        symbols = [1]
        smallest = part2()
        theOnes = str(smallest.FindString(symbols, k))
        if  theOnes[0] == '1' and len(theOnes) == 10962 and theOnes == len(theOnes) * theOnes[0]:
            print(" Test case 2 passed")
        else:
            print(" Test case 2 failed")

        # Test case 3
        k = 135
        symbols = [1, 3, 7]
        smallest = part2()
        if str(smallest.FindString(symbols, k)) == "No solution":
            print(" Test case 3 passed")
        else:
            print(" Test case 3 failed")



if __name__ == "__main__":
    main()