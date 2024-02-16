def is_permutation(s1, s2):
    flag_1 = 1
    flag_2 = 1
    for i in s2.lower():
        if i not in s1:
            flag_1 = 0
            break

    for j in s1.lower():
        if j not in s2:
            flag_2 = 0
            break

    if(flag_1 or flag_2):
        return True
    else:
        return False

def main():
  s1 = input()
  s2 = input()
  print('YES' if is_permutation(s1, s2) else 'NO')

if __name__ == '__main__':
  main()
