from Bio import AlignIO

def execute_aligned(fileName, outputFileName):
    input_handle = open(fileName, 'r')
    output_handle = open(outputFileName, 'w')
    alignments = AlignIO.parse(input_handle, 'fasta')
    AlignIO.write(alignments, output_handle, 'fasta')
