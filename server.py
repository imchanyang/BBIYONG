from flask import Flask, render_template, Response
from streamer import stream

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stream')
def video_feed():
    return Response(stream(), mimetype='multipart/x-mixed-replace; boundary=frame')



