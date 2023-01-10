from flask import Flask, request

app = Flask(__name__)

"""Basic math operations."""

@app.route('/add')
def add():
    '''
    Add a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a + b

@app.route('/sub')
def sub():
    '''
    Subtract b from a
    '''
    a = request.args['a']
    b = request.args['b']
    return a - b

@app.route('/mult')
def mult():
    '''
    Multiply a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a * b

@app.route('/div')
def div():
    '''
    Divide a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a / b
