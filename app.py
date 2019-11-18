from flask import Flask, escape, request, render_template, send_from_directory

from s3_downloader import S3Downloader

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    # Check if there is a new ODM file on s3 and if so, download it and send it to the frontend
    s3_client = S3Downloader()
    file = s3_client.poll_bucket()
    return render_template('landing.html', file=file)


@app.route('/statics/assets/<path:path>')
def send_js(path):
    return send_from_directory('statics/assets', path)

@app.route('/statics/data/<path:path>')
def send_data(path):
    return send_from_directory('statics/data', path)