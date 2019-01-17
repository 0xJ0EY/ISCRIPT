def vierkant(m, n = 1):
    matrix = [[0 for x in range(m)] for x in range(m)]

    for x in range(m):
        for y in range(m):
            matrix[x][y] = point(x, y, matrix, n)

    return matrix

def point(x, y, matrix, n):
    if x == 0 or y == 0: return n

    point1 = matrix[x][y - 1]
    point2 = matrix[x - 1][y]

    return point1 + point2

def paden(m, n = 1):
    matrix = vierkant(m, n)
    length = len(str(matrix[m - 1][m - 1]))
    output = []

    for x in range(m):
        line = ""

        for y in range(m):
            line += repr(matrix[x][y]).rjust(1 + length)

        output.append(line + '\n')

    return ''.join(output)

def main():
    print(paden(3))
    print(paden(3, 100))
    print(paden(4))
    print(paden(6))
    print(paden(8))
    print(paden(10))

if __name__ == "__main__":
    main()