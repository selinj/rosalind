s = 'TGCCGATCGGCTCAGTATGTGGGACGGAGCATAATCGAAGATGGCGTTTTGCATGCTCCGGCTGGCTCCGATTATGCGCGGGGTCGTCTTCCAGACGCTTGAAAGCATCCAAGTCCCGATTCCCCTCCCTAAGGGTCAGTTCCACCTAGTTTGTTCGCTGTCTAGTACTGAAGACGCGTATTGCGCTCGACGATATCCCACTGAAGTAACCCCACGAATTAATGTTAGTCATGGCGAACTCAATTCGATGGTTGTGAGCTCATCGATATAAAATAAAGGCCTAACCATAACCGGCGTTTTACGAAAACTGGTTTCTCTGGGGAGCTCTAAGGGCTGACGCCGCAGGCGCTTGGTAGGCGGTAGCAGGTGCCGGGTTACGCCGGTAATTTACAGCTGTCACACGATAGCGTTGATGGGATAGACGAGCGAAGACGCTTAGAAGGTTGTGTCCACCCAGTCGGCCTGGCTTGTGAACTGGTCTAGATGAAAAATAATTAACTCTACAGTTCGCCGGCTGGCTTTAGCGCTTCGCAAAGTTCGCCCGAAGCGACCTCAGGCATTCCTGTAATTGGCCACAGTAGTCTGACTGAATCTAGACACTCTATTCTTATAGTTTCTAATAGGGTGACCACGGGTGTATTCCCAGATAAAGTTTAGAAGGACTGTATAAAAGTTTTACGCCGGCGCGGATAACAAACGGGGTTCCCGTGAGACCATTTAACTCATGAGGGGACATCACCGTTCCAGCACAACCGCACTCCGCCATCGCAACTTACGTCCCACTGCCGTCCATACAGATTGCCACATTAATCCTTTTACGACAGCCAAGCGGTGCACGCATAGTCTAAGATCTGGGTGGGATTTTACCTGGTTTTAAATCGGAAAAGAGTACACCACTATTTGAGCGACGTACGCCCGGTCTCAGACGAACCTTTGATCGTTTGTATGTG'


index = 0
counter = 0
for x in s:
    counter = counter + 1

##for i in s:   
##    if i == 'T':
##        s.replace('T', 'U');
##    index = index + 1
       

print s.replace('T', 'U')
