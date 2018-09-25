complimentary_nucleotides_rna_dna = {'A': 'T', 'U': 'A', 'C': 'G', 'G': 'C'}
complimentary_nucleotides_rna = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and U")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides_rna[nt.upper()] for nt in self.sequence))

    @property
    def dna_sequence(self):
        return ''.join(complimentary_nucleotides_rna_dna[nt.upper()] for nt in self.sequence[::-1])