"""prints the number of pairs of DNA bases in ecoli.fasta"""
import problem2
#The import allows us to gain the code from the assigned file.
count_2=problem2.countpairs("ecoli.fasta")

problem2.printDigrams(count_2)