from flask import Blueprint, render_template, request, flash, redirect

from website import db
from .models import Service

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")


@views.route('/rezerwacja', methods=['GET', 'POST'])
def rezerwacja():
    services = Service.query.all()
    if request.method == "POST":
        # Get data from form called name;
        data = request.form.get("service_id")

        return render_template("reservation2.html", service=Service.query.get(int(data)))
    else:

        return render_template("reservation.html", services=services, show_modal=False)
