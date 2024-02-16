with open("example.txt", "r") as file:
    content = file.read()

words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in content).split()

max_length = max(len(word) for word in words)

for word in words:
    if len(word) == max_length:
        print(word)
