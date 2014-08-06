from flask import Blueprint, render_template, request


mod = Blueprint('entry', __name__, template_folder='views')


@mod.route('/')
def root():
    return render_template('entry.json')
