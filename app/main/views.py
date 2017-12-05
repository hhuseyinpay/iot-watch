from . import main
from .form import SignUp
from flask import request, render_template
from app.db.models import EUsers
from ..db.business_logic.user import UserBusinessLogic


@main.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUp(request.form)

    if request.method == 'POST':

        if form.validate_on_submit():
            new_user = EUsers(form.ssn.data, form.first_name.data, form.last_name.data, form.user_name.data,
                              form.password.data, form.description.data)

            result = UserBusinessLogic.insert(new_user)

        if result is None:
            return render_template('okey.html', username=new_user.username)
        else:
            return render_template('error_page.html', message=result)

    return render_template('signup.html', form=form)


@main.route("/userlist")
def userlist():
    users = UserBusinessLogic.select()
    print(users)
    return render_template('userlist.html', userlist=users)
