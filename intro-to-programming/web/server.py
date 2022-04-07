from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/employees', methods=['GET'])
def employees():
    return render_template('employees.html', employees = [])

if __name__ == "__main__":
    app.run()
