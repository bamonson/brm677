"""finds the number of pairs of DNA bases in ecoli.fasta"""
def countpairs(filename):
#def marks the start of function header
    with open(filename,'r') as input_file:
        string=input_file.read()
    #In Python you need to give access to a file by opening it. You can do it by using the open() function.
    counts = {}
    #The above defines the dictionary called counts
    string_length= len(string)
    for index in range(string_length):
    #Using a for loop to go through the data and continue to repeat.
        pair = string[index: index+2]
        #We are defining pairs to show we want the value and the value after it.
        if pair in counts:
            counts[pair] += 1
        else:
            counts[pair] = 1
    return counts

from typing import Dict

def printDigrams (pairsCount: Dict[str, int]):
    "Print the diagrams"

    bases = ['A', 'G', 'C', 'T']

    # Print the column headings
    print(' ', end=' ')
    for ch in bases:
        # Using a for loop to go through the characters and continue to repeat.
        print(ch.rjust(7), end=' ')
    print()


    # Print the body of the table
    for ch1 in bases:
        print(ch1, end=' ')

        # Print a row of the table
        for ch2 in bases:
            # Using a for loop to go through the characters and continue to repeat.
            digram = ch1 + ch2
            if (digram in pairsCount):
                count = pairsCount[digram]
            else:
                count = 0

            # Print count, with formating
            print(repr(count).rjust(7), end=' ')
        print()


