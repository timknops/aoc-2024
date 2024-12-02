with open("input.txt", "r") as f:
    data = [tuple(map(int, line.split())) for line in f]

data = [t for t in data if len(set(t)) == len(t)]

valid_data = []
for t in data:
    is_decreasing = all(t[i] >= t[i + 1] for i in range(len(t) - 1))
    is_increasing = all(t[i] <= t[i + 1] for i in range(len(t) - 1))

    valid_differences = all(abs(t[i] - t[i + 1]) <= 3 for i in range(len(t) - 1))

    if (is_decreasing or is_increasing) and valid_differences:
        valid_data.append(t)

print(len(valid_data))

