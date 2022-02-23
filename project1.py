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

if __name__ == "__main__":
    main()