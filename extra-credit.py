from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    try:
        numbers = request.json['numbers']
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("illegal argument type")
        return jsonify(result=sum(numbers))
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        a = request.json['a']
        b = request.json['b']
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("illegal argument type")
        return jsonify(result=a - b)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        numbers = request.json['numbers']
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("illegal argument type")
        result = 1
        for num in numbers:
            result *= num
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/divide', methods=['POST'])
def divide():
    try:
        a = request.json['a']
        b = request.json['b']
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("illegal argument type")
        if b == 0:
            raise ValueError("divide by zero")
        return jsonify(result=a / b)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/modulo', methods=['POST'])
def modulo():
    try:
        a = request.json['a']
        b = request.json['b']
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("illegal argument type")
        if b == 0:
            raise ValueError("divide by zero")
        return jsonify(result=a % b)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
