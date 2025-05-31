with open('input.txt', 'r') as f:
    a, b = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write(str(a + b) + "\n")