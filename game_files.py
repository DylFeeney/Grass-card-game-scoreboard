import csv


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
