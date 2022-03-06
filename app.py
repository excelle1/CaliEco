from flask import Flask, render_template
from replit import web
import lob
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
  return 'Wassup'

web.run(app)