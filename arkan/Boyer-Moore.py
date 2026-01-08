




def bad_character_table(pattern):
    """
    Membentuk tabel bad character
    (indeks terakhir setiap karakter pada pattern)
    """
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore_search(text, pattern):
    """
    Implementasi algoritma Boyer–Moore
    menggunakan Bad Character Rule
    """
    bad_char = bad_character_table(pattern)
    n = len(text)
    m = len(pattern)
    shift = 0  # posisi pattern pada text

    while shift <= n - m:
        j = m - 1  # mulai dari karakter paling kanan pattern

        # Bandingkan dari kanan ke kiri
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # Jika seluruh pattern cocok
        if j < 0:
            return True

        # Jika terjadi mismatch
        else:
            mismatch_char = text[shift + j]
            shift += max(1, j - bad_char.get(mismatch_char, -1))

    return False

text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

if boyer_moore_search(text, pattern):
    print("Pattern ditemukan dalam text")
else:
    print("Pattern tidak ditemukan")
