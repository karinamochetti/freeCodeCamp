def detect_mutations(strand1, strand2):
    return [idx for idx in range(len(strand1)) if strand1[idx] != strand2[idx]]

print(detect_mutations("ATCG", "ATGG"))
print(detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"))
print(detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"))
print(detect_mutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"))
print(detect_mutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT"))
