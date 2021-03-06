#!/usr/bin/python
"""All the url routing happens here. We need to import some things from flask, and we also import some functions
from the api that are defined in a separate module"""
from flask import Flask, render_template, jsonify
from api import weather_by_zip, fibonacci


# We define our app here, but we run it in the main.py file
app = Flask(__name__)


# app.route decorator routes activity to and from URLs
@app.route('/')
def render_home():
    return render_template('home.html')


# Most of these functions simply render templates
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


@app.route('/kivy/example')
def render_kivy_example():
    return render_template('kivy_example.html')


@app.route('/linux')
def render_linux():
    return render_template('linux.html')


@app.route('/my_contribution')
def render_my_contribution():
    return render_template('my_contribution.html')


@app.route('/sql')
def render_sql():
    return render_template('sql.html')


@app.route('/api')
def render_api():
    return render_template('api.html')


# Here, instead of rendering a template, we return date in JSON format
@app.route('/api/weather/<zipcode>')
def serve_weather_json(zipcode):
    return jsonify(weather_by_zip(zipcode))


# Here we serve a range of Fibonacci numbers in JSON
@app.route('/api/fibonacci/<number>')
def serve_fibonacci(number):
    fibs = {}
    try:
        start = int(number.split('-')[0])
        end = int(number.split('-')[1]) + 1
    except IndexError:
        start = int(number)
        end = int(number) + 1
    except TypeError:
        return jsonify('Invalid Entry')
    try:
        for i in range(start, end):
            fibs[i] = int(fibonacci(int(i)))
    except Exception as e:
        print e

    return jsonify(fibs)
