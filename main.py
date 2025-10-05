from flask import Flask ,render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('maintenance.html')

@app.route("/error")
def error():
    return "Error Page"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
