#!/usr/bin/python
from flask import Flask, render_template, jsonify
from api import weather_by_zip


app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('home.html')


@app.route('/python')
def render_python():
    return render_template('python.html')


@app.route('/about')
def render_about():
    return render_template('about.html')


@app.route('/flask')
def render_flask():
    return render_template('flask.html')


@app.route('/scraping')
def render_scraping():
    return render_template('scraping.html')


@app.route('/kivy')
def render_kivy():
    return render_template('kivy.html')


@app.route('/linux')
def render_linux():
    return render_template('linux.html')


@app.route('/my_contribution')
def render_my_contribution():
    return render_template('my_contribution.html')


@app.route('/api')
def render_api():
    return render_template('api.html')


@app.route('/api/weather/<zipcode>')
def serve_weather_json(zipcode):
    return jsonify(weather_by_zip(zipcode))
