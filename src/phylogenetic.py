import shutil
import subprocess
from datetime import datetime

from fastaUtilities import Fasta
from alignSequences import execute_aligned

def execute_phylogenetic_tree(fileName, bootstrap):
    fasta = Fasta(fileName)
    time = datetime.now().strftime("%Y-%b-%d_%H-%M-%S")
    if fasta.is_aligned():
        shutil.copy(fileName, f'{time}_aligned_{fileName}')
    else:
        execute_aligned(fileName)
    generate_phylogenetic_tree(f'{time}_aligned_{fileName}', bootstrap)


def generate_phylogenetic_tree(fileName, bootstrap):
    subprocess.call(f"iqtree -s ./{fileName} -bb {bootstrap}")
