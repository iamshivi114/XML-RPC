from xmlrpc.server import SimpleXMLRPCDispatcher
from flask import Flask, request
import sys

app = Flask(__name__)
dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)

def add(*args):
    if not all(isinstance(arg, int) for arg in args):
        return "illegal argument type"
    return sum(args)

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "divide by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "divide by zero"
    return a % b

dispatcher.register_function(add, 'add')
dispatcher.register_function(subtract, 'subtract')
dispatcher.register_function(multiply, 'multiply')
dispatcher.register_function(divide, 'divide')
dispatcher.register_function(modulo, 'modulo')

@app.route('/RPC', methods=['POST'])
def handle_rpc():
    response = dispatcher._marshaled_dispatch(request.data)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
