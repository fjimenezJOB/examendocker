from flask import Flask, render_template, redirect, url_for, request
import os


app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run('0.0.0.0', port=port, debug=True)