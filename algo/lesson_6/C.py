n = int(input())
sequence = list(map(int, input().split()))
len_subsequence = [1 for _ in sequence]
parents = [None for _ in sequence]

min_subsequence = 1

for i in range(1, n):
    for j in range(i)[::-1]:
        if sequence[i] > sequence[j]:

            if len_subsequence[j] >= len_subsequence[i]:
                len_subsequence[i] = len_subsequence[j] + 1
                parents[i] = j

max_subsequence_len = max(len_subsequence)
max_subsequence_index = len_subsequence.index(max_subsequence_len)
subsequence = []

while max_subsequence_index is not None:
    subsequence.append(sequence[max_subsequence_index])
    max_subsequence_index = parents[max_subsequence_index]

print(max_subsequence_len)
print(' '.join(map(str, subsequence[::-1])))
