import time
from KMP import kmp_search
from BM import boyer_moore_search


# ===============================
# DATA UJI
# ===============================
text = ("kemarin ada udin dateng kerumah terus dia nginjek eek tibatiba dia pengen eek yaudah deh terbang ke selatan untuk bertemu mamanya. " )
pattern = "eek"


# ===============================
# UJI KMP
# ===============================
start = time.perf_counter()
kmp_positions = kmp_search(text, pattern)
end = time.perf_counter()

kmp_time = end - start


# ===============================
# UJI BOYER-MOORE
# ===============================
start = time.perf_counter()
bm_positions = boyer_moore_search(text, pattern)
end = time.perf_counter()

bm_time = end - start


# ===============================
# OUTPUT
# ===============================
print("=== HASIL UJI STRING MATCHING ===")
print(f"Panjang dokumen : {len(text)} karakter")
print(f"Panjang pola    : {len(pattern)} karakter\n")

print("KMP")
print(f"Jumlah kemunculan : {len(kmp_positions)}")
print(f"Waktu eksekusi    : {kmp_time:.6f} detik\n")

print("Boyer-Moore")
print(f"Jumlah kemunculan : {len(bm_positions)}")
print(f"Waktu eksekusi    : {bm_time:.6f} detik")
