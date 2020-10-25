from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'To generate load, please visit /start - N.B. Once started the instance will need to be restarted as, for brevity, process handling has not been included'

@app.route('/start')
def start():
    os.system('dd if=/dev/zero of=/dev/null')

