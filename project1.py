# Currently, part 1 works for count == 6, does not work for count == 56
from part1 import part1

def main():
    print("Enter an integer for the length of the string")
    length = input()

    DFACount = part1()
    print("Number of possible strings of size " + str(length) + " that map to our language: " + str(DFACount.count(int(length))))

if __name__ == "__main__":
    main()