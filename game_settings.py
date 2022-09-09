from flask import request, render_template, Blueprint

game_options = Blueprint('game_options', __name__, template_folder='templates')


@game_options.route('/game-options', methods=['POST', 'GET'])
def game_options_page():
    if request.method == 'POST':
        print("POST")
    return render_template('game_options.html')
