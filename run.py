from flask import Flask
import os

app = Flask(__name__)

@app.route("/detect")
def runDetectPy():
    os.system('py detect.py --weights ./cars1000s.pt --img 416 --conf 0.4 --source ./video720.mp4')
    return ("ok")


if __name__ == '__main__':
    app.run(debug=True)