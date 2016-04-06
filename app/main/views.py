from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm

# view function for the index page, GET and POST methods
@main.route('/', methods=['GET', 'POST'])
def index():
    # build the form
    form = NameForm()
    if form.validate_on_submit():
        # the ORM models on user
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            # add the user to db
            db.session.add(user)
            # store data in session
            session['known'] = False
            # if the admin has been defined
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('main/index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))