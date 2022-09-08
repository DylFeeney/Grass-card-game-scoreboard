from flask import request, render_template, Blueprint
import csv

game_files_setup = Blueprint('game_files_setup', __name__, template_folder='templates')
@game_files_setup.route('/game-files-setup', methods=['POST', 'GET'])
def game_files_setup_page():
    return render_template('games_files_setup.html')


def create_new_game_files(rounds=[1]):
    """
    Create a new game, re-creates all the game files to 'reset' them all. The optional parm rounds can be populated to
    create more than 1 round.
    :param rounds: Pass in the number of rounds to create in a list e.g [1, 2, 3,] will create three rounds
    :return:
    """
    generate_user_file()
    # Only going to generate 1 round
    round_info_file(rounds)
    processed_round_info_files(rounds)


def generate_user_file():
    f = open('game_files/user_info.csv', 'w+')
    writer = csv.writer(f, lineterminator='\n')
    user_name_row = ['user_name']
    writer.writerow(user_name_row)
    f.close()


def create_multiple_file(round_numbers, file_path_front, file_path_back, fields):
    for i in range(len(round_numbers)):
        create_single_file(round_numbers[i], file_path_front, file_path_back, fields)


def create_single_file(round_number, file_path_front, file_path_back, fields):
    file_path = file_path_front + str(round_number) + file_path_back
    f = open(file_path, 'w+')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(fields)
    f.close()


def round_info_file(round_numbers):
    file_path_front = "game_files/round_information_files/round_information_"
    file_path_back = ".csv"
    round_information_row = ['round_number', 'user_name', 'protected_peddle', 'unprotected_peddle',
                             'highest_peddle_in_hand',
                             'has_banker', 'has_sold_out', 'has_double_crossed', 'has_utterly_wiped_out']
    create_multiple_file(round_numbers, file_path_front, file_path_back, round_information_row)


def processed_round_info_files(round_numbers):
    file_path_front = "game_files/round_processed_files/processed_round_information_"
    file_path_back = ".csv"
    fields = ['user_name', 'protected_peddle', 'unprotected_peddle', 'highest_peddle_in_hand', 'has_banker',
              'has_sold_out', 'has_double_crossed', 'has_utterly_wiped_out', 'net_profit']
    create_multiple_file(round_numbers, file_path_front, file_path_back, fields)
