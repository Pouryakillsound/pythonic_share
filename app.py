#!/bin/python3
import os
import argparse
from inspect import getsourcefile
from flask import Flask, render_template, send_from_directory
from collections import deque
from pathlib import Path

SOURCE_FILE_PATH = Path(__file__).resolve().parent
CURRENT_PATH = os.getcwd()
TEMPLATE_DIR = f'{SOURCE_FILE_PATH}/static'
print(TEMPLATE_DIR)
USERNAME = os.getlogin()
PROGRAM_NAME = 'pythonic share'
app = Flask(__name__, template_folder=TEMPLATE_DIR)

parser = argparse.ArgumentParser(prog=PROGRAM_NAME)
parser.add_argument('-d', '--directory', action='store', default='~/Downloads')
args = parser.parse_args()
path = deque([i for i in args.directory])

if path[0] == '~':
  path.popleft()
  path.appendleft(f'/home/{USERNAME}')

path = ''.join(path)

try:
  files = [i.name for i in os.scandir(path) if i.is_file()]
except FileNotFoundError:
  print('This directory doesn\'t exist')
  exit(1)
@app.route('/')
def hello_world():
  print(path, files)
  return render_template('router_home_page.html', files=files)


@app.route('/download/<path:name>')
def download_file(name, path=path):
  print(f'Someone is picking up <{name}> in >> {path}')
  return send_from_directory(path, name, as_attachment=True)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
