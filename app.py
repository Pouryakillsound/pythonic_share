import os
from flask import Flask, render_template, send_from_directory

PROGRAM_NAME = 'easy share'
template_dir = os.path.abspath('./static')
app = Flask(__name__, template_folder = template_dir)

path = os.getenv('path', ".")
path_abs = os.path.abspath(path)
files = [i.name for i in os.scandir(path_abs) if i.is_file()]


@app.route('/')
def hello_world():
    return render_template("router_home_page.html", files=files)

@app.route('/download/<path:name>')
def download_file(name, path=path_abs):
    print(path, name)
    return send_from_directory(path, name, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',  port='5000')
