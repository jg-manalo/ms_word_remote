from flask import Flask, render_template
import subprocess
app = Flask(__name__)

def runScript():
    res = subprocess.run(["C:\Program Files (x86)\Microsoft Office\Root\Office16\winword.exe"], shell=True, capture_output=True, text=True)
    print(res.stdout)


@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/word")
def word():
    runScript()
    return render_template("success.html")
if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.75', port=5000)