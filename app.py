from flask import Flask, request, g, redirect, url_for, render_template

app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
# ---------- MAIN PAGES ---------- #
@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')

@app.route('/complex')
def complex_home():
    return render_template('complex/complex.html')

@app.route('/about')
def about():
    return render_template('about.html')

# ---------- COMPLEX ANALYSIS ---------- #

@app.route('/complex/triangle-inequality')
def complex_triangle_inequality():
    return render_template('complex/triangle-inequality.html')

@app.route('/complex/cauchy-integral')
def cauchy_integral():
    return render_template('complex/cauchy-integral.html')

if __name__ == '__main__':
    app.run()
