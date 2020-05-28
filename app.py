from flask import Flask

import config

app = Flask(__name__)

@app.route("/")
def hello():
    return "there is no easter eggs here go away_ https://pbs.twimg.com/media/ECx9rziU8AAzDB4?format=jpg&name=small"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
