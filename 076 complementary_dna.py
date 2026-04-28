def complementary_dna(strand):
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(mapping[base] for base in strand)

print(complementary_dna("ACGT"))
print(complementary_dna("ATGCGTACGTTAGC"))
print(complementary_dna("GGCTTACGATCGAAG"))
print(complementary_dna("GATCTAGCTAGGCTAGCTAG"))
