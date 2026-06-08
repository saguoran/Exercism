def to_rna(dna_strand: str):
    nucleotides = str.maketrans('GCTA', 'CGAU')
    rna_strand = dna_strand.translate(nucleotides)
    return rna_strand

