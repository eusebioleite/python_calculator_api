from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    data = request.get_json()  # Get JSON data from the request body
    formula = data.get('formula')  # Get the value of the 'name' key from JSON data
    response = jsonify(eval(formula))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
