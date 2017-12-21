from . import main
from .form import SignUpForm, LoginForm, NameDescriptionForm, IDNameDescriptionForm, IDForm
from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from app.db.business_logic.user import UserBusinessLogic
from app.db.business_logic.admin import AdminBusinessLogic
from app.db.business_logic.device_type import DeviceTypeBusinessLogic
from app.db.business_logic.location import LocationBusinessLogic
from app.db.business_logic.measurement_type import MeasurementTypeBusinessLogic
from app.db.business_logic.measurement import MeasurementBusinessLogic
from app.db.business_logic.reporting_device import ReportingDeviceBusinessLogic


@main.route("/", methods=['GET'])
@login_required
def index():
    if current_user.admin is True:
        admin = True
    else:
        admin = None

    location_id = request.args.get('location_id')
    device_id = request.args.get('device_id')

    data = None
    if device_id:
        data = MeasurementBusinessLogic.get_data_by_device(device_id)

    devices = None
    if location_id is not None:
        devices = ReportingDeviceBusinessLogic.get_by_location(location_id)

    location = LocationBusinessLogic.get_all()
    meas_type = "Deneme"
    last = MeasurementBusinessLogic.get_last_measured_ipaddress()
    last_meas = last[0]
    last_local_ip = last[1]

    return render_template('index.html', data=data, meas_type=meas_type, devices=devices, locations=location,
                           last_meas=last_meas, last_local_ip=last_local_ip, admin=admin)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = UserBusinessLogic.get_user(form.ssn.data)
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for('main.index'))
        flash('wrong ssn or password')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route("/admin/login", methods=['GET', 'POST'])
def adminlogin():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        admin = AdminBusinessLogic.get_admin(form.ssn.data)
        if admin is not None and check_password_hash(admin.password, form.password.data):
            login_user(admin)
            return redirect(url_for('main.index'))
        flash('wrong ssn or password')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@main.route("/signup", methods=['GET', 'POST'])
@login_required
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        ret = UserBusinessLogic.create(form.ssn.data, form.firstname.data, form.lastname.data,
                                       form.username.data, form.password.data, form.description.data)

        if ret is None:
            return redirect(url_for('main.login'))
        else:
            return ret
    return render_template('signup.html', form=form)


@main.route("/admin", methods=['GET'])
@login_required
def admin():
    if current_user.admin is not True:
        return render_template('403.html')

    return render_template('admin.html')


@main.route("/admin/device_types", methods=['GET', 'POST'])
@login_required
def device_types():
    if current_user.admin is not True:
        return render_template('403.html')

    device_type = DeviceTypeBusinessLogic.get_all()
    return render_template('device_types.html', device_types=device_type)


@main.route("/admin/locations", methods=['GET', 'POST'])
@login_required
def locations():
    if current_user.admin is not True:
        return render_template('403.html')

    form = None
    form2 = None
    form3 = None

    if 'submit1' in request.form:
        form = NameDescriptionForm()
    if 'submit2' in request.form:
        form2 = IDNameDescriptionForm()
    if 'submit3' in request.form:
        form3 = IDForm()

    if form is not None:
        if form.validate_on_submit():
            ret = LocationBusinessLogic.create(form.name.data, form.description.data)
            if ret is None:
                flash("Adding is successfull")
            else:
                flash(ret)

    if form2 is not None:
        if form2.validate_on_submit() and form2.submit2.data:
            print("form2")
            LocationBusinessLogic.update(int(form2.id.data), form2.name.data, form2.description.data)

    if form3 is not None:
        if form3.validate_on_submit() and form3.submit3.data:
            print("form3")
            LocationBusinessLogic.delete(int(form3.id.data))

    if form is None:
        form = NameDescriptionForm(formdata=None, obj=...)
    if form2 is None:
        form2 = IDNameDescriptionForm(formdata=None, obj=...)
    if form3 is None:
        form3 = IDForm(formdata=None, obj=...)

    location = LocationBusinessLogic.get_all()
    return render_template('locations.html', form=form, form2=form2, form3=form3, locations=location)


@main.route("/admin/measurement_types")
@login_required
def measurement_types():
    if current_user.admin is not True:
        return render_template('403.html')

    measurement_type = MeasurementTypeBusinessLogic.get_all()
    return render_template('measurement_types.html', measurement_types=measurement_type)


@main.route("/admin/measurements")
@login_required
def measurements():
    if current_user.admin is not True:
        return render_template('403.html')

    measurement = MeasurementBusinessLogic.get_all()
    return render_template('measurements.html', measurements=measurement)


@main.route("/admin/reporting_devices")
@login_required
def reporting_devices():
    if current_user.admin is not True:
        return render_template('403.html')

    reporting_device = ReportingDeviceBusinessLogic.get_all()
    return render_template('reporting_devices.html', reporting_devices=reporting_device)


@main.route("/admin/users")
@login_required
def users():
    if current_user.admin is not True:
        return render_template('403.html')
