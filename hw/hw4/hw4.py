from flask import Flask, render_template, url_for, request, redirect
import collections
import matplotlib.pyplot as plt
import json

NAMES = ['gender', 'age', 'region', 'olimpname']
app = Flask(__name__)


@app.route('/')
def index():
    if request.args:
        olimpname = request.args['olimpname']
        age = request.args['age']
        gender = request.args['gender']
        region = request.args['region']
        with open('data.csv', 'a', encoding='utf-8') as t:
            row = '%s\t%s\t%s\t%s\n' % \
                  (gender, age, region, olimpname)
            t.write(row)
        return redirect(url_for('stats'))
    return render_template('index.html')


@app.route('/stats')
def stats():
    c = collections.Counter()
    with open('data.csv', encoding='utf-8') as f:
        table = f.read()
    table = table.replace('\n', '\t').split('\t')
    tmp = table[3::4]
    for word in tmp:
        c[word] += 1
    dat = [c[key] for key in c]
    lables = list(c)
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title('Использование названий в %', size=16)
    plt.pie(dat, labels=lables, autopct='%1.1f%%')
    plt.savefig('static/plot1.png', format='png')
    return render_template('stat.html')


@app.route('/search')
def search():
    res = []
    with open('data.csv', encoding='utf-8') as f:
        table = f.read().strip('\n')
    table = table.split('\n')
    for line in table:
        res.append(line.split('\t'))
    word = request.args.get('word', '')
    gender = request.args.getlist('gender')
    gender_i = NAMES.index('gender')
    result = [r for r in res if r[gender_i]
              in gender and any(word in w for w in r[1:4])]
    return render_template('search.html', results=result)


@app.route('/json')
def getjson():
    with open('data.csv', encoding='utf-8') as f:
        table = f.read().strip('\n')
    res = [{n: v for n, v in zip(NAMES, line.split('\t'))}
           for line in table.split('\n')]
    data = json.dumps(res, ensure_ascii=False, indent=4)
    return render_template("json.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)

