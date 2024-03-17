from flask import Flask, render_template  # Import functions and classes from flask

app = Flask(__name__)  # Define Flask class


@app.route("/")
def index():
    return render_template("index.html",  # Name of the file in /templates
                           directory="index",  # Name of the directory in /static/styles and /static/scripts
                           script=True,  # If the page contains a JavaScript file
                           title="Title")  # Title of the page


if __name__ == "__main__":  # If the script is being directly ran
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run on all IPs on port 5000 with debugging
