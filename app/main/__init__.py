from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@main.route('/characters', methods=['GET', 'POST'])
def characters():

    return render_template('characters.html')


@main.route('/register', methods=['GET', 'POST'])
def register():

    return render_template('register.html')


@main.route('/guides')
def guides():

    return render_template('guides.html')