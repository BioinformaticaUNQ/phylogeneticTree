import shutil
import subprocess
from datetime import datetime

from fastaUtilities import Fasta
from alignSequences import execute_aligned

def execute_phylogenetic_tree(fileName, bootstrap):
    fasta = Fasta(fileName)
    time = datetime.now().strftime("%Y-%b-%d_%H-%M-%S")
    outputFile = f"{time}_aligned_{fileName}"
    if fasta.is_aligned():
        shutil.copy(fileName, outputFile)
    else:
        execute_aligned(fileName, outputFile)
    generate_phylogenetic_tree(outputFile, bootstrap)


def generate_phylogenetic_tree(fileName, bootstrap):
    subprocess.call(f"iqtree -s ./{fileName} -bb {bootstrap}", shell=True)
    print("Done!")
