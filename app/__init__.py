from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KYZX234'

from app import views