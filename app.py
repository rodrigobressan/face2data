from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Index page goes here!"


if __name__ == '__main__':
    print('Starting Flask server')
    app.run()
    # app.run(host='0.0.0.0', port=7000, debug=True)
