def shift_matrix(matrix):
    n = len(matrix)
    for level in range(n // 2):
        if level % 2 != 0:
            temp = matrix[level][level]
            for i in range(level, n - level - 1):
                matrix[level][i] = matrix[level][i + 1]
            for i in range(level, n - level - 1):
                matrix[i][n - level - 1] = matrix[i + 1][n - level - 1]
            for i in range(n - level - 1, level, -1):
                matrix[n - level - 1][i] = matrix[n - level - 1][i - 1]
            for i in range(n - level - 1, level, -1):
                matrix[i][level] = matrix[i - 1][level]
            matrix[level + 1][level] = temp
        else:
            temp = matrix[level][level]
            temp_1 = matrix[level][n - level - 1]
            temp_2 = matrix[n - level - 1][level]
            for i in range(level, n - level - 1):
                matrix[n - level - 1][i] = matrix[n - level - 1][i + 1]
            for i in range(level, n - level - 1):
                matrix[i][level] = matrix[i + 1][level]
            for i in range(n - level - 1, level, -1):
                matrix[level][i] = matrix[level][i - 1]
            for i in range(n - level - 1, level, -1):
                matrix[i][n - level - 1] = matrix[i - 1][n - level - 1]
            matrix[level + 1][n - level - 1] = temp_1
            matrix[n - level - 2][level] = temp_2
            matrix[level][level + 1] = temp


def analyze_and_append(matrix, output_filename):
    n = len(matrix)

    # Analyze matrix and append 1 or 0 based on column ordering
    ordered_columns = all(matrix[i][j] <= matrix[i + 1][j] for j in range(n - 1) for i in range(n - 1))

    with open(output_filename, 'a') as out_file:
        out_file.write("\n" + str(int(ordered_columns)))


def main(input_filename, output_filename):
    # Read matrix from input file
    with open(input_filename, 'r') as in_file:
        matrix = [list(map(int, line.split())) for line in in_file.readlines()]

    # Process the matrix according to the rules
    shift_matrix(matrix)

    # Write the modified matrix to output file
    with open(output_filename, 'w') as out_file:
        for row in matrix:
            out_file.write(' '.join(map(str, row)) + '\n')

    # Analyze the matrix and append information to output file
    analyze_and_append(matrix, output_filename)


if __name__ == "__main__":
    input_file = "in.txt"
    output_file = "out.txt"

    main(input_file, output_file)
