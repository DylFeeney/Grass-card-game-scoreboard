from flask import Flask, render_template
from game_files import round_info_file, processed_round_info_files

app = Flask(__name__)


@app.route('/')
def index():
    round_numbers = [1, 2, 3, 4, 5]
    round_info_file(round_numbers)
    round_numbers_two = [6]
    round_info_file(round_numbers_two)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
