def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    

    L[0] = last_item

def lines_startswith_1(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))

    return matches


def lines_startswith_2(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    matches.append(line.startswith(letter).rstrip('\n'))

    return matches


def lines_startswith_3(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    return matches


def lines_startswith_4(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.
    The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []

    for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))

    return matches
