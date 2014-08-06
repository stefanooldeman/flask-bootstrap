from flask import Blueprint, render_template, request, url_for, redirect

from {{package}} import base_url, url_version


mod = Blueprint('entry', __name__, template_folder='views')


@mod.route('/')
def root():
    return render_template('entry.json')
