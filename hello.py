from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
def hello(name='Pizda'):
    return render_template('hello.html', name=name)


@app.route('/99-bottles')
def bottles():
    return render_template('bottles.html',
                           title='bottles!',
                           number_of_bottles=99
                           )


@app.route('/args/', methods=['GET'])
def args():
    # test = request.args.items(multi=True)
    # test1 = request.args.items(multi=True)
    # return render_template('table.html', test=test, test1=test1)
    rows = []
    for arg in request.args:
        rows.append((arg, list(request.args.getlist(arg))))
    return render_template('table.html', rows=rows)

# http://127.0.0.1:5000/args/?arg1=Hello&arg2=world&arg1=Dude
