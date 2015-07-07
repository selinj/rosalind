
'''using the first example in the problem, the protein with
uniprot id B5ZC00'''

s='MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK'

#N-glycosylation motif: N{P}[ST]{P}

listofindexes = []
index = 0

for i in range(len(s)-5):
    if s[i] == 'N':
        #go on
        index = i
        if s[i+1] != 'P':
            if s[i+2] == 'S' or s[i+2] == 'T':
                if s[i+3] != 'P':
                    listofindexes.append(i+1)
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue

print listofindexes
