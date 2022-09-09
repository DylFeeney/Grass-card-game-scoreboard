from flask import Flask, render_template
from game_files import create_new_game_files
from game_files import game_files_setup
from game_settings import game_options

app = Flask(__name__)
app.register_blueprint(game_files_setup)
app.register_blueprint(game_options)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
