def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    >>> is_valid_sequence('ATCGTAAGCT')
    True
    >>> is_valid_sequence('GTACRTC')
    False
    """

    validity = True

    for nucleotide in dna:
        if nucleotide not in 'ATCG':
            validity = False

    return validity

def insert_sequence(dna1, dna2, position):
    """ (str, str, int) -> str

    Return a dna string which is produced by taking dna1 and inserting dna2 at
    specified position.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATG', 'CCC', 0)
    'CCCATG'
    >>> insert_sequence('GGTCC', 'A', -2)
    'GGTACC'
    """

    dna = dna1[0:position] + dna2 + dna1[position:len(dna1)]
    
    return dna 

def get_complement(nucleotide):

    """ (str) -> str

    Return the complementary nucleotide to a given nucleotide. 

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    if nucleotide == 'A':
        nucleotide_complementary = 'T'
    elif nucleotide == 'T':
        nucleotide_complementary = 'A'
    elif nucleotide == 'C':
        nucleotide_complementary = 'G'
    elif nucleotide == 'G':
        nucleotide_complementary = 'C'

    return nucleotide_complementary

def get_complementary_sequence(dna):

    """ (str) -> str

    Return the complementary strand to a given dna. 

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('TCCGATG')
    'AGGCTAC'
    """

    dna_complementary = ''

    for nucleotide in dna:

        dna_complementary = dna_complementary + get_complement(nucleotide)

    return dna_complementary
