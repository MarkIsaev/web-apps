def minion_game(string):
    vowels = 'AEIOU'
    kevin_score, stuart_score = 0, 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Кевин", kevin_score)
    elif kevin_score < stuart_score:
        print("Стюарт", stuart_score)
    else:
        print("Ничья")

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)
