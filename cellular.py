import sys
import random

rule = int(sys.argv[1]) if len(sys.argv) > 1 else 18
rand = int(sys.argv[2]) if len(sys.argv) > 2 else 0
lines = int(sys.argv[3]) if len(sys.argv) > 3 else 31
width = int(sys.argv[4]) if len(sys.argv) > 4 else 100

def display(line):
    print("".join("#" if x == 1 else " " for x in line))

# from 000 to 111 by increment of 1
ruleset = []
for i in range(0,8):
    n = rule % (2 << i)
    ruleset.append(1 if n != 0 else 0)
    rule -= n

data = []
result = []
# First Line (all zero, with a single 1 in middle)
for i in range(width):
    data.append(0)
if rand == 0:
    data[int(len(data)/2)] = 1
else:
    count = random.randrange(width)
    for i in range(count):
        data[random.randrange(width)] = 1
result.append(data.copy())
# Lines in Succession
for n in range(lines):
    new_data = []
    for i in range(0, len(data)):
        if i == 0:
            rule = data[width - 1] << 2 | data[i] << 1 | data[i + 1]
        elif i == len(data) - 1:
            rule = data[width - 1] << 2 | data[i] << 1 | data[0]
        else:
            rule = data[i - 1] << 2 | data[i] << 1 | data[i + 1]
        new_data.append(ruleset[rule])
    data = new_data.copy()
    result.append(data.copy())

for n in range(len(result)):
    display(result[n])