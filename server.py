from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def everyone():
    img = '/static/img/tmnt.png'
    return render_template('ninja.html', img = img)

@app.route('/ninja/<color>')
def tmnt(color):
    print(color)
    if color == 'red':
        img = '/static/img/raphael.jpg'
    elif color == 'blue':
        img = '/static/img/leonardo.jpg'
    elif color == 'orange':
        img = '/static/img/michelangelo.jpg'
    elif color == 'purple':
        img = '/static/img/donatello.jpg'
    else:
        img = '/static/img/notapril.jpg'
    return render_template('ninja.html', img = img)

if __name__=="__main__":
    app.run(debug = True)    