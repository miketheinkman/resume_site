#!/usr/bin/python
from flask import Flask, render_template, request, redirect
from data import *

app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template('home.html')