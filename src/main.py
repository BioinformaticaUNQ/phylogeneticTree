import sys

from phylogenetic import execute_phylogenetic_tree
from exception import ModelException

try:
    args = sys.argv
    execute_phylogenetic_tree(args[1], args[2])
except ModelException as e:
    print(f"ERROR: {e.message}")
    sys.exit(0)
