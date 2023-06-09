"""
Credits:https://github.com/anzeljg/flask-examples
"""

# Import Flask modules
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import HTTPException

# Import Flask WTForms modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Import Flask SQLAlchemy modules
from flask_sqlalchemy import SQLAlchemy

# Import other modules
from datetime import datetime

# ========== Create application ========== #

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


# ========== Route definitions ========== #
#
#  HTTP method | URL path          | Controller function
# -------------+-------------------+----------------------
#  GET         | /                 | list_posts()
#  GET         | /posts            | list_posts()
#  GET, POST   | /post/add         | add_post()
#  GET, POST   | /post/edit/<id>   | edit_post(id)
#  GET, POST   | /post/delete/<id> | delete_post(id)
#  GET         | /post/view/<id>   | view_post(id)
# -------------+-------------------+----------------------
#

# Index page for entry web application
@app.route('/', methods=['GET'])
@app.route('/posts', methods=['GET'])
def list_posts():
    # Get all entry posts, the newest first
    records = db.session.query(Entrypost).order_by(Entrypost.created.desc()).all()

    return render_template('index.html', data=records)


# Add new entry post
@app.route('/post/add', methods=['GET', 'POST'])
def add_post():
    # Setup form
    form = AddPostForm()

    # Process form; no default values here
    if form.validate_on_submit():
        # Handle creating entry post in the database
        if request.method == 'POST' and 'submit' in request.form:
            # Save entry post to the database
            timestamp = datetime.now()
            record = Entrypost(
                created=timestamp,
                updated=timestamp,
                title=request.form.get('title'),
                content=request.form.get('content')
            )
            db.session.add(record)
            db.session.commit()

        return redirect(url_for('list_posts'))

    return render_template('add.html', title='Add post', form=form)


# Edit and update existing entry post
@app.route('/post/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    # Get existing entry post by id
    record = db.session.query(Entrypost).get(id)

    # Setup form
    form = EditPostForm(obj=record)

    # Process form; no default values here
    if form.validate_on_submit():
        # Handle updating entry post in the database
        if request.method == 'POST' and 'submit' in request.form:
            # Update entry post in the database
            timestamp = datetime.now()
            record.updated = timestamp
            record.title = request.form.get('title')
            record.content = request.form.get('content')
            db.session.commit()

        return redirect(url_for('list_posts'))

    return render_template('edit.html', title='Edit post', form=form)


# Delete existing entry post
@app.route('/post/delete/<id>', methods=['GET', 'POST'])
def delete_post(id):
    # Get existing entry post by id
    record = db.session.query(Entrypost).get(id)

    # Setup form
    form = DeletePostForm()

    # Process form; no default values here
    if form.validate_on_submit():
        # Handle deleting entry post from the database
        if request.method == 'POST' and 'submit' in request.form:
            # Delete entry post from the database
            db.session.delete(record)
            db.session.commit()
            # flash('Entrypost was successfully deleted.')

        return redirect(url_for('list_posts'))

    return render_template('delete.html', title='Delete post', form=form)


# View and read entry post
@app.route('/post/view/<id>', methods=['GET', 'POST'])
def view_post(id):
    # Get existing entry post by id
    record = db.session.query(Entrypost).get(id)

    return render_template('view.html', title='View post', data=record)


# Handle HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(error):
    return render_template('error.html', error=error), error.code


# ========== Form definitions ========== #

# Form to add entry post
class AddPostForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired('You must provide entry title!')]
    )
    content = TextAreaField(
        'Content',
        validators=[DataRequired('You must provide entry content!')]
    )
    submit = SubmitField('Add')


# Form to edit entry post
class EditPostForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired('You must provide entry title!')]
    )
    content = TextAreaField(
        'Content',
        validators=[DataRequired('You must provide entry content!')]
    )
    submit = SubmitField('Edit')


# Form to delete entry post
class DeletePostForm(FlaskForm):
    submit = SubmitField('Delete')


# ========== Database model definitions ========== #

# Database model for Entrypost entity
class Entrypost(db.Model):
    __tablename__ = 'entrypost'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def __init__(self, created, updated, title, content):
        self.created = created
        self.updated = updated
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Entrypost %r>' % self.title


# ========== Create DB with default values ========== #

with app.app_context():
    # Create the database/tables if it/they don't exist yet
    # This call has to be after database model definitions!
    db.create_all()

    # Check if test data exist in the database
    exists = Entrypost.query.first()

    # Welcomes new users who have no diary entries, by adding a starting entry
    if not exists:
        timestamp = datetime.now()
        posts = [
            Entrypost(
                created=timestamp,
                updated=timestamp,
                title='Welcome to Diary-oh!',
                content='To write your own diary entry simply press the green button on the right!'
            )
        ]
        for post in posts:
            db.session.add(post)
        db.session.commit()

# ========== Run application ========== #

if __name__ == '__main__':
    # Run application and development server
    app.run(debug=True)
