#!/usr/bin/python
from flask import Flask, render_template, request, redirect


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