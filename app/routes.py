from flask import render_template, url_for, redirect, flash
from app import app, bcrypt, db
from app.models import loginn
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user


@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = loginn.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', login=True, form=form)

@app.route("/index")
@app.route("/home")
# @login_required
def index():
    pageData = {
        "breadcrumb": "Dashboard",
        "pageHeader": "Dashboard",
        "pages": "dashboard.html"
    }
    return render_template('index.html', pageData=pageData, index=True)

@app.route("/profile")
@login_required
def profile():
    pageData = {
        "breadcrumb": "Profile",
        "pageHeader": "Profile",
        "pages": "profile.html"
    }
    return render_template('index.html', pageData=pageData, profile=True)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = loginn(nama=form.nama.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', register=True, form=form)

@app.route("/masuk")
@login_required
def masuk():
    pageData = {
        "breadcrumb": "Riwayat Masuk Kendaraan",
        "pageHeader": "Riwayat Masuk Kendaraan",
        "pages": "masuk.html"
    }
    return render_template('index.html', pageData=pageData, masuk=True)

@app.route("/keluar")
@login_required
def keluar():
    pageData = {
        "breadcrumb": "Riwayat Keluar Kendaraan",
        "pageHeader": "Riwayat Keluar Kendaraan",
        "pages": "keluar.html"
    }
    return render_template('index.html', pageData=pageData, keluar=True)

@app.route("/admin")
@login_required
def admin():
    pageData = {
        "breadcrumb": "Daftar Admin",
        "pageHeader": "Daftar Admin",
        "pages": "admin.html"
    }
    return render_template('index.html', pageData=pageData, admin=True)

@app.route("/pengguna")
@login_required
def pengguna():
    pageData = {
        "breadcrumb": "Daftar Pengguna",
        "pageHeader": "Daftar Pengguna",
        "pages": "pengguna.html"
    }
    return render_template('index.html', pageData=pageData, pengguna=True)

@app.errorhandler(404)
def notfound(error):
    return render_template('error.html')

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You are Logged out', 'success')
    return redirect(url_for('login'))