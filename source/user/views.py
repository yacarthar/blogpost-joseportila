from flask import Blueprint, render_template, request, url_for, session, redirect
from flask_login import login_required, login_user, logout_user

from source import db
from source.models import User, Post
from source.forms import LoginForm, RegisterForm, UpdateForm



user = Blueprint('user', __name__)


@user.route('register', methods=['POST', 'GET'])
@login_required()
def register()
	form = RegisterForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		password = form.password.data
		new_user = User(name, email, password)
		db.session.add(new_user)
		db.session.commit()
		redirect(url_for('user.login'))
	return render_template('register.html', form=form)


@user.route('login', methods=['POST', 'GET'])
@login_required()
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user_check = User.query.filter_by(username=form.name.data)
		if user_check is not None and user_check.check_password(orm.name.password):
			login_user()
			flask('login success')
			next = request.args.get('next')
			if next == None or next['/'] != '/':
				next = url_for('core.index')
			return redirect(next)
	return render_template('login.html', form=form)


@user.route('logout')
def logout():
	logout_user()



@user.route('account')
@user.route('posts')

