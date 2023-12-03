def swap_case(s):
    #s.swapcase()
    swapped_s = ''
    for ch in s:
        if ch.islower():
            swapped_s += ch.upper()
        elif ch.isupper():
            swapped_s += ch.lower()
        else:
            swapped_s += ch
        
    return swapped_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)