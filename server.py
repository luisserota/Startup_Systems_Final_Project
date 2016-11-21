from flask import Flask
from flask import render_template, request, redirect, url_for, abort
import PythonMagick


app = Flask(__name__)


@app.route('/')
def root():
	image = PythonMagick.Image("http://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/110.png&w=350&h=254")
	return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0')