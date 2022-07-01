from Bio import pairwise2
import sys


def verificar_vregion_imgt(queryGeneCode, seqGeneCode, dictionary):

    maior_score = 0
    seq_result = ""
    query_result = ""
    alignments = ""
    result = ""
    len_vregion = 0

    for key in dictionary:
        alignments = pairwise2.align.globalxx(seqGeneCode, dictionary[key])
        result = pairwise2.format_alignment(*alignments[0])
        score = int(result.split("=")[1])
        if score > maior_score:
            maior_score = score
            seq_result = result
            query_result = key
            len_vregion = len(dictionary[key])


    #return seq_result
    #Estou imprimindo a sequencia original sem \n para imprimir esta na mesma linha
    print(queryGeneCode + " - " + query_result.replace(">", "").lstrip())
    print(seq_result)
    print("LEN-SEQ-GENE-CODE|LEN-VREGION=" + str(len(seqGeneCode)) + "|" + str(len_vregion))


def create_dictonary(caminhoFileVregionImgt):

    fileVregion = open(caminhoFileVregionImgt, "r")
    dictionary = {}
    query = ''

    for linha in fileVregion:

        if (linha.find(">") > -1):
            query = linha.upper()

        else:
            dictionary[query] = linha.upper()
            query = ''

    fileVregion.close()

    return dictionary


caminhoFileGeneCode = sys.argv[1]
caminhoFileVregionImgt = sys.argv[2]

#Criando um dicionario com a V-REGION
dictionary = create_dictonary(caminhoFileVregionImgt)

#Abrir o arquivo com as sequencias do GENECODE e S
fileGeneCode = open(caminhoFileGeneCode, "r")

query = ""
for linha in fileGeneCode:
    if (linha.find(">") > -1):
        query = linha.replace('\n', '')
        #print(linha)

    else:
        verificar_vregion_imgt(query, linha.upper(), dictionary)

fileGeneCode.close()


#seqVregion = "caggtgcagctggtgcagtctggggctgaggtgaagaagcctggggcctcagtgaaggtctcctgcaaggcttctggatacaccttcaccggctactatatgcactgggtgcgacaggcccctggacaagggcttgagtggatgggatggatcaaccctaacagtggtggcacaaactatgcacagaagtttcagggcagggtcaccatgaccagggacacgtccatcagcacagcctacatggagctgagcaggctgagatctgacgacacggccgtgtattactgtgcgagaga"
#seqVregion = seqVregion.upper();
#seqGeneCodeT = "GAGAGCATCACCCAGCAACCACATCTGTCCTCTAGAGAATCCCCTGAGAGCTCCGTTCCTCACCATGGACTGGACCTGGAGGATCCTCTTCTTGGTGGCAGCAGCCACAGGTAAGAGGCTCCCTAGTCCCAGTGATGAGAAAGAGATTGAGTCCAGTCCAGGGAGATCTCATCCACTTCTGTGTTCTCTCCACAGGAGCCCACTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGGCCTCAGTGAAGGTCTCCTGCAAGGCTTCTGGATACACCTTCACCGGCTACTATATGCACTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGATGGATCAACCCTAACAGTGGTGGCACAAACTATGCACAGAAGTTTCAGGGCAGGGTCACCATGACCAGGGACACGTCCATCAGCACAGCCTACATGGAGCTGAGCAGGCTGAGATCTGACGACACGGCCGTGTATTACTGTGCGAGA"
#alignments = pairwise2.align.globalxx("ACCGT", "ACG")
#print(*alignments[0])
