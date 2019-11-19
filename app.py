from flask import Flask, escape, request, render_template

from s3_downloader import S3Downloader

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    # Check if there is a new ODM file on s3 and if so, download it and send it to the frontend
    s3_client = S3Downloader()
    file = s3_client.poll_bucket()
    return render_template('landing.html', file=file)


