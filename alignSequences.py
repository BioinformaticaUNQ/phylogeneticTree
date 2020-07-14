from Bio import AlignIO

def execute_aligned(fileName):
    input_handle = open(fileName, 'r')
    output_handle = open(f'aligned_{fileName}', 'w')
    alignments = AlignIO.parse(input_handle, 'fasta')
    AlignIO.write(alignments, output_handle, 'fasta')
