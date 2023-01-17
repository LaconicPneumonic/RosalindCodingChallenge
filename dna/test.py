from collections import Counter
testInput = "TTTACTTCATTCCTTGAAAGAATTGAGGGAACTCAACACCCTATGTCCGATACCGTAGCTCGACCTAGGACCATTAGAAACGACTCTACTGCCTTGCATGGATGAAGGCACAACTGAACTTCCTGCAGTGAAAGTGTGAGCCCTGACCACTCCCGAGGGTTTGTGTGGTTCTCCTTGGGTTACGTGATAGTTATTAAGCTATTCGGGTAACGTACATGCGTACAAGGAGAATCTACTCAAATATTCGGCGGTGATTGTACTTGCCCTTACGTCGATTAGTTGCTTATTTAGATCTATTTCAGTCTTGTGCCGCCTGCTATTGATACAGCAACGACAGGCTTTGAGGCATCGGCGCGCAGCATGCGCTTATCCGTGTTATCAATTGGAGTATTCAGCTTTCAAAAGTGTGAGTAAGTTTTTAGATATCGTGTCTCGTCGTCCAGAGCCTCTGCCCCCATTTCATTAGACATAGTGAAATATGAGCTTAGCCACAAAACCAAAATTGGAACATGTGCTCAACTTTCTAGTACATATGGCATGGTGCTATATACGAAGCGCTACTCCCCCGTACATGAAGCCCCCAACGACTTGATACCTGGAACGTAGCAATATAATTTATCACGTTATTGCTTTGAACGACTGATATCATGGCTGCGTAGGGCAGTCCACAACGGTATGGTAAACCTACTCTTTTCCAGACATGAGGCCCGGGTAGAGTAAGGAGTCGGAATTAGGAAGAGGCCTAAATGCCGGTTATGCCAGCCGGCTATTCGCGGAGACTCGACTATCGGATGTTCCCATGGGAAGTTGAGCGAGTGAATAAGACGCAACCTTTTATGGGTCATTGTTATATTTACTCAAATGGGCCAGCCAGAATTTAAAGCTATGCTTC"


c = Counter(testInput)

print(c)

print(" ".join([str(c[a]) for a in 'ACGT']))