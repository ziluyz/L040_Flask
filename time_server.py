from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def show_time():
    return """
    <html>
    <body>
    <h1>The current time is:</h1>
    <p>{}</p>
    </body>
    </html>
    """.format(time.ctime())

if __name__ == '__main__':
    app.run()
