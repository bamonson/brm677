"""finds the number of bases in ecoli.fasta in the terminal."""
def counting(filename):
#def marks the start of function header
    filename_split = filename.split('.')

    assert(len(filename_split) == 2)
    assert(filename_split[1] == 'fasta')

    counter_A = counter_C = counter_G = counter_T = 0


    with open(filename,'r') as input_file:
    #In Python you need to give access to a file by opening it. You can do it by using the open() function.
        input_file.readline()
        for line in input_file:
            my_line=line.strip()
            for character in my_line:
                if character =='A':
                    counter_A += 1
                elif character == 'C':
                    counter_C+=1
                elif character == 'G':
                    counter_G+=1
                elif character == 'T':
                    counter_T+=1
                else:
                    print('character |',character,'|')
                    raise NameError()
    print('As:',counter_A)
    print('Cs:',counter_C)
    print('Gs:',counter_G)
    print('Ts:',counter_T)