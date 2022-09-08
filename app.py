from flask import Flask, render_template
from game_files import create_new_game_files

app = Flask(__name__)


@app.route('/')
def index():
    create_new_game_files([1,2,3])
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
