from . import main
from .form import SignUpForm, LoginForm
from flask import request, render_template, redirect, url_for
from app.db.models.user import UserModel
from app.db.business_logic.user import UserBusinessLogic
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user


@main.route("/", methods=['GET', 'POST'])
@login_required
def index():
    data = [('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0),
            ('Date(2016,12,15,11,30,0,0)', 65.9, 35.0, 40.0), ('Date(2017,12,15,11,30,0,0)', 35.9, 15.0, 20.0),
            ('Date(2016,12,15,10,30,0,0)', 72.9, 45.0, 27.0), ('Date(2016,11,15,11,30,0,0)', 17.9, 22.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 68.9, 85.0, 39.0), ('Date(2016,11,15,11,30,0,0)', 32.9, 29.0, 41.0),
            ('Date(2016,12,15,10,30,0,0)', 76.9, 58.0, 21.0), ('Date(2016,11,15,11,30,0,0)', 82.9, 32.0, 48.0),
            ('Date(2016,12,15,10,30,0,0)', 99.9, 51.0, 45.0), ('Date(2016,11,15,11,30,0,0)', 6.9, 3.0, 41.0)
            ]
    devices = ["Deneme1","Deneme2"]
    return render_template('index.html', data=data, devices=devices)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = UserBusinessLogic.get_user(form.ssn.data)
        print(user.ssn)
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for('main.index'))

    return render_template('login.html', form=form)


@main.route("/signup", methods=['GET', 'POST'])
#@login_required
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = UserModel(ssn=form.ssn.data, firstname=form.firstname.data, lastname=form.lastname.data,
                         username=form.username.data,
                         password=generate_password_hash(form.password.data, method='sha256'),
                         description=form.description.data)
        ret = UserBusinessLogic.create(user)

        if ret is None:
            return "OK"
        else:
            return "sıkıntı bilaader"
    return render_template('signup.html', form=form)
