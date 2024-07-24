#!/bin/python3
import os
import argparse
from sys import exit
from pathlib import Path
from collections import deque
from flask import Flask, render_template, send_from_directory

OS = os.name
Windows = 'nt'
Unix_like = 'posix'
SOURCE_FILE_PATH = Path(__file__).resolve().parent
CURRENT_PATH = os.getcwd()
TEMPLATE_DIR = f'{SOURCE_FILE_PATH}/static'
USERNAME = os.getlogin()
PROGRAM_NAME = 'pythonic share'
app = Flask(__name__, template_folder=TEMPLATE_DIR)

parser = argparse.ArgumentParser(prog=PROGRAM_NAME)
if OS == Unix_like:
  parser.add_argument('-d', '--directory', action='store', default='~/Downloads')
elif OS == Windows:
  parser.add_argument('-d', '--directory', action='store', default=fr'C:\Users\{USERNAME}\Downloads')

args = parser.parse_args()
share_path = deque([i for i in args.directory])

if share_path[0] == '~' and OS == Unix_like:
  share_path.popleft()
  share_path.appendleft(f'/home/{USERNAME}')
elif share_path[0] == '~' and OS == Windows:
  print('<~> operator is not supported on windows')
  exit(1)

if share_path[0] == '.':
    share_path.popleft()
    share_path.appendleft(os.path.abspath(CURRENT_PATH))

share_path = ''.join(share_path)

try:
  files = [i.name for i in os.scandir(share_path) if i.is_file()]
except FileNotFoundError:
  print('This directory doesn\'t exist')
  exit(1)

@app.route('/')
def hello_world():
  return render_template('router_home_page.html', files=files)


@app.route('/download/<path:name>')
def download_file(name, path=share_path):
  print(f'Someone is picking up <{name}> in >> {path}')
  return send_from_directory(path, name, as_attachment=True)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
