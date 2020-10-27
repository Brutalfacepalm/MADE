source_string = list(input())
end_line = list(input())

distance_matrix = [[1 * i for i in range(len(end_line) + 1)]] + \
                  [[1 * (j + 1) for _ in range(len(end_line) + 1)] for j, _ in enumerate(source_string)]

for i in range(1, len(source_string) + 1):
    for j in range(1, len(end_line) + 1):
        if source_string[i - 1] == end_line[j - 1]:
            distance_matrix[i][j] = distance_matrix[i - 1][j - 1]
        else:
            distance_matrix[i][j] = min(distance_matrix[i - 1][j - 1], distance_matrix[i - 1][j],
                                        distance_matrix[i][j - 1]) + 1

print(distance_matrix[-1][-1])
