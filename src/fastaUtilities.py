import re
from exception import ModelException

validCharacters = re.compile("([ABCDEFGHIKLMNOPQRSTUVWXYZ\\-\\*]+)")

def read_fasta(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    content = dict([])
    header = None
    for line in lines:
        if line.startswith(">"):
            header = line
            content[header] = ""
        else:
            content[header] += line.rstrip("\n")
    return content

class Fasta:
    def __init__(self, fileName):
        self.content = read_fasta(fileName)
        self._check_has_sequences()
        self._check_sequences_for_valid_characters()
        self._check_sequences_for_same_type()
        self.isAligned = self._check_alignment()

    def _check_sequences_for_valid_characters(self):
        errors = []
        for header, seq in self.content.items():
            if validCharacters.match(seq).group(1) != seq:
                errors.append(header)                
        if errors:
            raise ModelException(f"Sequences not valid: {errors}")

    def _check_sequences_for_same_type(self):
        numberOfUniqueCharacters = [len(set(seq)) for seq in self.content.items()]
        if all(characters >= 4 for characters in numberOfUniqueCharacters):
            self.seqType = "PROTEIN"
            return
        if all(characters <= 4 for characters in numberOfUniqueCharacters):
            self.seqType = "DNA"
            return
        raise ModelException("Sequences with different type")

    def _check_has_sequences(self):
        if not self.content:
            raise ModelException(f"Not found sequences")

    def _check_alignment(self):
        length = None
        anyContainsGaps = False
        for seq in self.content.values():
            if not length:
                length = len(seq)
            if len(seq) != length:
                return False
            else:
                anyContainsGaps = anyContainsGaps or '-' in seq
        return anyContainsGaps

    def is_aligned(self):
        return self.isAligned

    def get_seq_type(self):
        return self.seqType
