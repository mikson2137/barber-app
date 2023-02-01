# import uuid
import shortuuid

from flask import Blueprint, render_template, request, flash, redirect

from website import db
from website.models import Note

views = Blueprint('views', __name__)


@views.route('/note_gen', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('notetitle')
        content = request.form.get('notecontent')

        if len(title) == 0 or len(content) == 0:
            flash("Title and content are required!", category='error')
            # return render_template("gen_note.html", isEmpty=True)
        else:
            link = shortuuid.uuid()[0:6]
            print(link)
            new_note = Note(title=title, content=content, link=link)
            db.session.add(new_note)
            db.session.commit()

            return redirect(f"/notes/{link}")
    else:
        return render_template("gen_note.html")


@views.route('/notes/<string:link>')
def notes(link):
    note = Note.query.filter_by(link=link).first()
    if note:
        return render_template("notes.html", note=note)
    else:
        return render_template("404.html")


@views.route('/')
def index():
    return render_template("index.html")


@views.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
