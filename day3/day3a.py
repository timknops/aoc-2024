import re

with open("input.txt", "r") as f:
    data = f.read()

matches = re.findall(r"mul\(\d+,\d+\)", data)
nums = [re.findall(r"\d+", match) for match in matches]
total = sum(int(x) * int(y) for x, y in nums)

print(total)

