from flask import Flask, escape, request, render_template

from s3_downloader import S3Downloader

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    target_name = request.args.get('listing_id', '')

    # Check if there is a new ODM file on s3 and if so, download it and send it to the frontend
    s3_client = S3Downloader()
    zip = s3_client.poll_bucket(target_name=target_name)
    return render_template('landing.html', file=zip)
