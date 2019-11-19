from flask import Flask, escape, request, render_template, send_from_directory

from s3_downloader import S3Downloader

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    # Check if there is a new ODM file on s3 and if so, download it and send it to the frontend
    s3_client = S3Downloader()
    file = s3_client.poll_bucket()
    return render_template('landing.html', file=file)

@app.route('/statics/<path:path>')
def send_js(path):
    return send_from_directory('statics', path)

@app.route('/include/<path:path>')
def send_include(path):
    return send_from_directory('statics/include', path)

@app.route('/jsmodeler/<path:path>')
def send_jsmodeler(path):
    return send_from_directory('statics/jsmodeler', path)

@app.route('/extensions/<path:path>')
def send_extensions(path):
    return send_from_directory('statics/extensions', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('statics/images', path)