import argparse
import seqops

parser = argparse.ArgumentParser()
parser.add_argument('sequences', type=str, help = 'at least one sequence for letter counting', nargs = '*')
parser.add_argument('-f', '--file', help = 'a file of sequences for letter counting')
arguments = parser.parse_args()

if arguments.file:
    seq_file = open(arguments.file, 'r') # reading from a file
    sequences = []
    for line in seq_file.readlines():
        seq = line.strip()
        sequences.append(seq)
else:
    sequences = arguments.sequences

for seq in sequences:
    seq = seqops.ensure_lowercase(seq)
    seqops.count_letters(seq)
