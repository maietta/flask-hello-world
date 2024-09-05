from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    # Watch the templates and static files for changes
    server.watch('templates/*.html')   # Watches HTML files
    server.watch('static/css/*.css')   # Watches CSS files
    # Start the livereload server
    server.serve(host='0.0.0.0', port=5000, debug=True)