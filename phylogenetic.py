import shutil

from fastaUtilities import Fasta
from alignSequences import execute_aligned

def execute_phylogenetic_tree(fileName):
    fasta = Fasta(fileName)
    if fasta.is_aligned():
        shutil.copy(fileName, f'aligned_{fileName}')
    else:
        execute_aligned(fileName)
    generate_phylogenetic_tree(f'aligned_{fileName}')


def generate_phylogenetic_tree(fileName):
    print('toDo')


execute_phylogenetic_tree('fasta.ft')
