nucleotides = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
def to_rna(dna_strand: str):
    try:
        return ''.join(map(nucleotides.__getitem__, dna_strand.upper()))
    except KeyError:
        return ''
