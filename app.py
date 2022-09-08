from flask import Flask, render_template
from game_files import create_new_game_files
from game_files import game_files_setup

app = Flask(__name__)
app.register_blueprint(game_files_setup)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
