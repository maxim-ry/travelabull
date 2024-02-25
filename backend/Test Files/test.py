from flask import Flask

test = Flask(__name__)

@test.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    test.run(debug=True)