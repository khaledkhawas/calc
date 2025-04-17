from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        # Basic safety for eval
        result = eval(expression, {'__builtins__': None}, {})
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
