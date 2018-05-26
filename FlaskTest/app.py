from flask import Flask,jsonify
import json
import TestFunctionLib

app = Flask(__name__)


@app.route('/')
def index():
	return "This is the home page"
@app.route('/about')
def about():
	return '<h2> About page </h2>'
@app.route('/functionTest/<call>')
def whatameme(call):
	return json.dumps(TestFunctionLib.testFunc(call))


if __name__ == "__main__":
	app.run(debug=True)