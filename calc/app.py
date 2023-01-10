from flask import Flask, request

app = Flask(__name__)

"""Basic math operations."""

# @app.route('/add')
# def add():
#     '''
#     Add a and b
#     '''
#     a = request.args['a']
#     b = request.args['b']
#     return str(int(a) + int(b))

# @app.route('/sub')
# def sub():
#     '''
#     Subtract b from a
#     '''
#     a = request.args['a']
#     b = request.args['b']
#     return str(int(a) - int(b))

# @app.route('/mult')
# def mult():
#     '''
#     Multiply a and b
#     '''
#     a = request.args['a']
#     b = request.args['b']
#     return str(int(a) * int(b))

# @app.route('/div')
# def div():
#     '''
#     Divide a and b
#     '''
#     a = request.args['a']
#     b = request.args['b']
#     return str(int(a) / int(b))

# SOMEHOW, I FORGOT THAT THERE ARE BUILT IN METHODS FOR ADD, SUBTRACT, MULTIPLY, AND DIVIDE

math = {
    'add': lambda a, b: a+b,
    'sub': lambda a, b: a-b,
    'mult': lambda a, b: a*b,
    'div': lambda a, b: a/b
}

@app.route('/math/<operation>')
def do_math(operation):
    '''
    Performs the requested math operation with the input values of a and b
    '''
    a = request.args['a']
    b = request.args['b']
    return str(math[operation](int(a), int(b)))