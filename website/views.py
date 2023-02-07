# import uuid
import shortuuid

from flask import Blueprint, render_template, request, flash, redirect

from website import db
from website.models import Note

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")


@views.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
