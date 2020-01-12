from flask import Flask, abort, jsonify, request

# result = []
# with open('result.txt', 'r') as f:
#     result.append(f.read())

# Flask App
app = Flask(__name__)
@app.route('/')
def hello():
    with open('result.txt', 'r') as f:
        return ", ".join(f.readlines())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
