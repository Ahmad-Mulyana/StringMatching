



def compute_lps(pattern):
    """
    Fungsi ini membentuk array LPS (Longest Prefix Suffix)
    """
    lps = [0] * len(pattern)
    length = 0  # panjang prefix-suffix terpanjang sebelumnya
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    """
    Fungsi ini mengimplementasikan algoritma KMP
    untuk mencari pattern di dalam text
    """
    lps = compute_lps(pattern)
    i = 0  # indeks text
    j = 0  # indeks pattern

    while i < len(text):
        # Jika karakter cocok, maju ke karakter berikutnya
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # Jika seluruh pattern cocok
        if j == len(pattern):
            return True

        # Jika terjadi mismatch
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                # Gunakan LPS untuk loncat
                j = lps[j - 1]
            else:
                i += 1

    return False

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

if kmp_search(text, pattern):
    print("Pattern ditemukan dalam text")
else:
    print("Pattern tidak ditemukan")
