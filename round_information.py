from flask import request, render_template, Blueprint
import json

round_information = Blueprint('round_information', __name__, template_folder='templates')


@round_information.route('/round-information', methods=['POST', 'GET'])
def round_information_page():
    if request.method == 'POST':
        print('POST')
    return render_template('round_information.html')