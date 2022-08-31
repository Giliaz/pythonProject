# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    chars = sorted(chars)
    for i in range(len(chars)):
        if i < len(chars) - 1:
            if (ord(chars[i + 1]) - ord(chars[i])) == 1:
                continue
            else:
                return chr(ord(chars[i]) + 1)

