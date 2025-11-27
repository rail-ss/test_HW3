from flask import Flask, request

app = Flask(__name__)

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - не числа', 400
    return str(a * b)

if __name__ == '__main__':
    app.run(debug=True)