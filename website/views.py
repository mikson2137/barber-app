from flask import Blueprint, render_template, request, flash, redirect

from website import db
from .models import Service

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")


@views.route('/rezerwacja', methods=['GET', 'POST'])
def rezerwacja():
    if request.method == "POST":
        return render_template("resstep2.html")
    else:
        services = Service.query.all()
        return render_template("reservation.html", services=services)
