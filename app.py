import os
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    #return "Hello from Python, prof Ruben!"
    return app.send_static_file('app.html')         #Return the HTML file for index page

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
