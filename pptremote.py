#!/usr/bin/python3
from flask import Flask
import logging
import sys
import os

LOGFILE = os.environ['HOME'] + "/pptremote/pptremote.log"

# Have flask use stdout as the logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.DEBUG)
c = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c.setFormatter(formatter)
main_logger.addHandler(c)

app = Flask(__name__)

@app.route('/next')
def next_endpoint():
    print('Next command')
    cmd = "xdotool getactivewindow key Right"
    os.system(cmd)
    return 'Next command'

@app.route('/prev')
def prev_endpoint():
    print('Prev command')
    cmd = "xdotool getactivewindow key Left"
    os.system(cmd)
    return 'Prev command'


@app.route('/endppt')
def escape_endpoint():
    print('Escape command')
    cmd = "xdotool getactivewindow key Escape"
    os.system(cmd)
    return 'Escape command'


@app.route('/startppt')
def startppt_endpoint():
    scommand = "startppt"
    cmd = "xdotool key F5"
    os.system(cmd)
    return 'Starting presentation'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
