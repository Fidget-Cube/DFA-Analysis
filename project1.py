# Currently, part 1 works for count == 6, does not work for count == 56
from part1 import part1

def main():
    DFACount = part1()
    print(DFACount.count(56))

if __name__ == "__main__":
    main()