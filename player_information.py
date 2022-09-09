from flask import request, render_template, Blueprint
import csv
import pandas as pd

player_information = Blueprint('player_information', __name__, template_folder='templates')


@player_information.route('/player-information', methods=['POST', 'GET'])
def user_information_page():
    if request.method == 'POST':
        player_name = request.form.get('player')
        player_name = player_name.upper()
        print(player_name)
        add_player_to_game(player_name)
    players = get_player_names()
    return render_template('player_info.html', players=players)


def get_player_names():
    df = pd.read_csv('game_files/player_info.csv')
    names = df['player_name']
    return names


def get_number_of_players():
    players = get_player_names()
    return len(players)


def add_player_to_game(player):
    fields = [player]
    with open(r'game_files/player_info.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(fields)