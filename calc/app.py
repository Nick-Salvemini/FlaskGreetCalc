from flask import Flask, request

app = Flask(__name__)

@app.source('/add')
def add():
    '''
    Add a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a + b

@app.source('/sub')
def sub():
    '''
    Subtract b from a
    '''
    a = request.args['a']
    b = request.args['b']
    return a - b

@app.source('/mult')
def mult():
    '''
    Multiply a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a * b

@app.source('/div')
def div():
    '''
    Divide a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return a / b
