def build_bad_character_table(pattern):
    """
    Tabel karakter buruk (bad character heuristic)
    """
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table


def boyer_moore_search(text, pattern):
    """
    Mengembalikan list posisi kemunculan pattern di text
    """
    bad_char = build_bad_character_table(pattern)
    positions = []

    m = len(pattern)
    n = len(text)
    s = 0  # shift shift an cuy

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            positions.append(s)
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return positions
