import math

[n, k] = list(map(int, input().split()))
costs = list(map(int, input().split()))
costs = [0] + costs + [0]
steps_positions = [[] for _ in costs]

for i, _ in enumerate(costs):
    dp_test_for_j = 0
    current_max = -math.inf
    if i != 0:
        for j in range(1, k + 1):
            if i - j >= 0:
                dp_test_for_j = costs[i - j]
                if dp_test_for_j > current_max:
                    current_max = dp_test_for_j
                    best_step = j
        steps_positions[i] += steps_positions[i - best_step]
        steps_positions[i].append(i - best_step + 1)
        costs[i] += current_max

dp = costs[-1]
steps_positions = steps_positions[-1]
print(dp)
print(len(steps_positions))
steps_positions.append(n)
print(' '.join(map(str, steps_positions)))
