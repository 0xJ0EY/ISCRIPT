def T9(string):
    result = []

    lookup_table = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 2,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'V': 9, 'W': 9, 'Y': 9, 'Z': 9
    }

    for char in string:
        result.append(str(value_from_table(char, lookup_table)))

    return ''.join(result)

def value_from_table(key, table):
    ans = table[key.upper()]

    return ans if ans > 0 else 0

def GSMoniemen(a, b):
    return T9(a) == T9(b)
