from flask import request, render_template, Blueprint
import json

game_options = Blueprint('game_options', __name__, template_folder='templates')


@game_options.route('/game-options', methods=['POST', 'GET'])
def game_options_page():
    if request.method == 'POST':
        banker, sold_out, doublecrossed, utterly_wiped_out, bonus, winning_value = get_game_options_from_form(request)
        game_options = update_game_options(banker, sold_out, doublecrossed, utterly_wiped_out, bonus, winning_value)
    elif request.method == 'GET':
        game_options = read_game_options()
    return render_template('game_options.html', game_options=game_options)


def get_game_options_from_form(incoming_request):
    banker = incoming_request.form.get('banker')
    sold_out = incoming_request.form.get('sold_out')
    doublecrossed = incoming_request.form.get('doublecrossed')
    utterly_wiped_out = incoming_request.form.get('utterly_wiped_out')
    bonus = incoming_request.form.get('bonus')
    winning_value = incoming_request.form.get('winning_value')
    return banker, sold_out, doublecrossed, utterly_wiped_out, bonus, winning_value


def update_game_options(banker, sold_out, doublecrossed, utterly_wiped_out, bonus, winning_value):
    game_options = read_game_options()

    game_options['banker'] = banker
    game_options['sold_out'] = sold_out
    game_options['doublecrossed'] = doublecrossed
    game_options['utterly_wiped_out'] = utterly_wiped_out
    game_options['bonus'] = bonus
    game_options['winning_value'] = winning_value

    with open('game_files/game_optons.json', 'w') as jsonFile:
        json.dump(game_options, jsonFile)

    return game_options

def read_game_options():
    with open('game_files/game_optons.json', 'r') as jsonFile:
        game_options_data = json.load(jsonFile)
    return game_options_data
