import os
from flask import Flask, render_template, request
import time
from pypdf import PdfReader
from docx import Document

# Import Algoritma
from kmp import kmp_search
from bm import boyer_moore_search

app = Flask(__name__)

def extract_text_from_file(file):
    filename = file.filename.lower()
    text = ""
    
    try:
        if filename.endswith('.pdf'):
            reader = PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        elif filename.endswith('.docx'):
            doc = Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif filename.endswith('.txt'):
            text = file.read().decode('utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
    
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    result_kmp = None
    result_bm = None
    time_kmp = 0
    time_bm = 0
    kmp_count = 0
    bm_count = 0
    
    text_input = ""
    pattern_input = ""
    
    # Default tab aktif (biar pas reload gak balik ke manual terus)
    active_tab = 'manual' 

    if request.method == 'POST':
        # 1. Ambil Pattern & Ubah ke Huruf Kecil (Case Insensitive)
        pattern_raw = request.form.get('pattern', '')
        pattern_input = pattern_raw.lower() # SOLUSI MASALAH 1

        # 2. LOGIKA BARU: Cek File Dulu, Baru Manual (SOLUSI MASALAH 2)
        uploaded_file = request.files.get('file_upload')
        
        if uploaded_file and uploaded_file.filename != '':
            # Jika user upload file
            print(f"File diterima: {uploaded_file.filename}") # Debugging di terminal
            text_input = extract_text_from_file(uploaded_file)
            active_tab = 'upload' # Biar tab upload tetap terbuka
        else:
            # Jika tidak ada file, ambil dari manual
            text_input = request.form.get('text_manual', '')
            active_tab = 'manual'

        # 3. Jalankan Algoritma (Hanya jika teks & pattern tidak kosong)
        if text_input and pattern_input:
            # Pastikan teks dokumen juga di-lowercase
            text_to_search = text_input.lower()

            # KMP
            start_time = time.perf_counter()
            result_kmp_list = kmp_search(text_to_search, pattern_input)
            end_time = time.perf_counter()
            
            time_kmp = (end_time - start_time) * 1000
            kmp_count = len(result_kmp_list)
            result_kmp = str(result_kmp_list)

            # Boyer-Moore
            start_time = time.perf_counter()
            result_bm_list = boyer_moore_search(text_to_search, pattern_input)
            end_time = time.perf_counter()
            
            time_bm = (end_time - start_time) * 1000
            bm_count = len(result_bm_list)
            result_bm = str(result_bm_list)
        else:
            print("Teks input kosong atau gagal diekstrak.")

    return render_template('index.html', 
                           text_preview=text_input[:500],
                           pattern=request.form.get('pattern', ''), # Kembalikan pattern asli (biar user liat)
                           result_kmp=result_kmp, 
                           result_bm=result_bm,
                           time_kmp=f"{time_kmp:.4f}", 
                           time_bm=f"{time_bm:.4f}",
                           kmp_count=kmp_count,
                           bm_count=bm_count,
                           active_tab=active_tab) # Kirim info tab mana yang aktif

if __name__ == '__main__':
    app.run(debug=True, port=5001)