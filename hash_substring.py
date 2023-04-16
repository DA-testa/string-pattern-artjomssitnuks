def read_input():

    first_input = input()
    if first_input.startswith("I"):
        pattern = input()
        text = pattern.rstrip()
    else:
        pattern = input()
        text = pattern.rstrip()
        
    return pattern, text




def print_occurrences(output):
    
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    p = 31
    m = len(pattern)
    n = len(text)
    p_pow = [1]
    for i in range(max(m, n) + 1):
        p_pow.append(p_pow[-1] * p)

    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash += ord(pattern[i]) * p_pow[m - i - 1]
        text_hash += ord(text[i]) * p_pow[m - i - 1]

    occurrences = []

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                occurrences.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * p_pow[m - 1]) * p + ord(text[i + m])

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
