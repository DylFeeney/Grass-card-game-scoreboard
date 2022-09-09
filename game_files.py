from flask import request, render_template, Blueprint
import csv
import json
import os
import pandas as pd

game_files_setup = Blueprint('game_files_setup', __name__, template_folder='templates')


@game_files_setup.route('/game-files-setup', methods=['POST', 'GET'])
def game_files_setup_page():
    if request.method == 'POST':
        number_of_rounds = int(request.form.get("number_of_rounds"))
        create_new_game = request.form.getlist("create_new_game")
        """
        If create_new_game is larger than 1 then create a new game. Input examples
        [0] - The box is not checked
        [0, 1] - The box is checked
        """
        if len(create_new_game) == 2:
            create_new_game_files(number_of_rounds=number_of_rounds)
        else:
            for i in range(number_of_rounds):
                add_new_round()
            print(number_of_rounds)
    return render_template('games_files_setup.html')


def delete_files(directory):
    for filename in os.listdir(directory):
        file = directory + "/" + filename
        os.remove(file)


def create_new_game_files(rounds=None, number_of_rounds=-1):
    """
    Create a new game, re-creates all the game files to 'reset' them all. The optional parm rounds can be populated to
    create more than 1 round.
    :param number_of_rounds: The number of rounds to create for the game
    :param rounds: Pass in the number of rounds to create in a list e.g [1, 2, 3,] will create three rounds
    :return:
    """
    # Delete the existing files in the directories
    delete_files("game_files/round_information_files")
    delete_files("game_files/round_processed_files")
    create_game_options()
    generate_user_file()
    round_numbers = get_round_numbers(rounds, number_of_rounds)
    generate_round_file(round_numbers)
    # Only going to generate 1 round
    round_info_file(round_numbers)
    processed_round_info_files(round_numbers)


def create_game_options():
    game_options = {
        "banker": 5000,
        "sold_out": -25000,
        "doublecrossed": -50000,
        "utterly_wiped_out": -100000,
        "bonus": 25000,
        "winning_value": 250000
    }
    # Serializing json
    json_object = json.dumps(game_options, indent=4)

    # Writing to game_optons.json
    with open('game_files/game_optons.json', "w+") as outfile:
        outfile.write(json_object)


def get_round_numbers(rounds, number_of_rounds):
    if number_of_rounds == -1:
        return rounds
    else:
        rounds = []
        number_of_rounds = number_of_rounds + 1
        for i in range(1, number_of_rounds):
            rounds.append(i)
        return rounds


def generate_user_file():
    f = open('game_files/user_info.csv', 'w+')
    writer = csv.writer(f, lineterminator='\n')
    user_name_row = ['user_name']
    writer.writerow(user_name_row)
    f.close()


def generate_round_file(rounds):
    f = open('game_files/rounds.csv', 'w+')
    writer = csv.writer(f, lineterminator='\n')
    fields = ['round_number', 'round_status']
    writer.writerow(fields)
    for i in range(len(rounds)):
        row = [rounds[i], 0]
        writer.writerow(row)
    f.close()


def get_rounds():
    """
    :return: rounds.csv file data
    """
    rounds = pd.read_csv('game_files/rounds.csv')
    return rounds


def add_new_round():
    rounds = get_rounds()
    last_round_number = rounds[-1:]['round_number'].values[0]
    new_round_number = last_round_number + 1
    fields = [new_round_number, 0]
    create_single_file("", "game_files/rounds", ".csv", fields, "a")


def create_multiple_file(round_numbers, file_path_front, file_path_back, fields, status):
    for i in range(len(round_numbers)):
        create_single_file(round_numbers[i], file_path_front, file_path_back, fields, status)


def create_single_file(round_number, file_path_front, file_path_back, fields, status):
    file_path = file_path_front + str(round_number) + file_path_back
    f = open(file_path, status)
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(fields)
    f.close()


def round_info_file(round_numbers):
    file_path_front = "game_files/round_information_files/round_information_"
    file_path_back = ".csv"
    status = "w+"
    round_information_row = ['round_number', 'user_name', 'protected_peddle', 'unprotected_peddle',
                             'highest_peddle_in_hand',
                             'has_banker', 'has_sold_out', 'has_double_crossed', 'has_utterly_wiped_out']
    create_multiple_file(round_numbers, file_path_front, file_path_back, round_information_row, status)


def processed_round_info_files(round_numbers):
    file_path_front = "game_files/round_processed_files/processed_round_information_"
    file_path_back = ".csv"
    status = "w+"
    fields = ['user_name', 'protected_peddle', 'unprotected_peddle', 'highest_peddle_in_hand', 'has_banker',
              'has_sold_out', 'has_double_crossed', 'has_utterly_wiped_out', 'net_profit']
    create_multiple_file(round_numbers, file_path_front, file_path_back, fields, status)
