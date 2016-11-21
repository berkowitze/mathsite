from flask import Flask, request, g, redirect, url_for, render_template
import os
from BeautifulSoup import BeautifulSoup

def insert_into(lst, item):
    if lst == []:
        return [item]
    else:
        if item[0] < lst[0][0]:
            return [item] + lst
        else:
            return [lst[0]] + insert_into(lst[1:], item)


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
    file_list = []
    for f in os.listdir('templates/complex/'):
        if f == 'complex-topics.html' or f == 'complex.html':
            continue

        fname = 'templates/complex/%s' % f
        url = 'complex/%s' % f.replace('.html', '')
        parsed_f = BeautifulSoup(open(fname).read())
        title = parsed_f.find('title').text
        order = int(parsed_f.find('order').text)
        item = (order, url, title)
        file_list = insert_into(file_list, item)
        print file_list

    print file_list
    return render_template('complex/complex.html', file_list=file_list)

@app.route('/about')
def about():
    return render_template('about.html')

# ---------- COMPLEX ANALYSIS ---------- #

@app.route('/complex/complex-numbers')
def complex_numbers():
    return render_template('complex/complex-numbers.html')

@app.route('/complex/polar-repr')
def polar_repr():
    return render_template('complex/polar-repr.html')

@app.route('/complex/triangle-inequality')
def complex_triangle_inequality():
    return render_template('complex/triangle-inequality.html')

@app.route('/complex/cauchy-integral')
def cauchy_integral():
    return render_template('complex/cauchy-integral.html')

if __name__ == '__main__':
    app.run()
