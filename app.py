from flask import Flask, render_template, request
import time
# Import file algoritma yang kita buat tadi
import kmp
import bm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_kmp = None
    result_bm = None
    time_kmp = 0
    time_bm = 0
    text = ""
    pattern = ""

    if request.method == 'POST':
        text = request.form['text']
        pattern = request.form['pattern']

        start_time = time.perf_counter() 
        algo_result_kmp = kmp.kmp_search(text, pattern)
        end_time = time.perf_counter() 
        time_kmp = (end_time - start_time) * 1000

        start_time = time.perf_counter()
        algo_result_bm = bm.bm_search(text, pattern)
        end_time = time.perf_counter()
        time_bm = (end_time - start_time) * 1000

        result_kmp = algo_result_kmp
        result_bm = algo_result_bm

    return render_template('index.html', 
                           text=text, 
                           pattern=pattern, 
                           result_kmp=result_kmp, 
                           result_bm=result_bm,
                           time_kmp=f"{time_kmp:.4f}",
                           time_bm=f"{time_bm:.4f}")

if __name__ == '__main__':
    app.run(debug=True, port=5001)