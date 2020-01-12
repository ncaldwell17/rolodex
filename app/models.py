"""
This file defines the database structure/schema for the application. Every
new datafile needs to be a class that passes in a db.Model object as an
argument.

This file 'cannot' change the database as it adds classes/items without
recreating it from scratch. Instead, Alembic (the migration framework
used by the package Flask-Migrate) will allow you to do this without recreating
the database.

Alembic maintains a migration repo, which is a directory that it stores migration
scripts. This repo is created using the command line.

Once a class has been added, or a class' attributes have been changed, run
$ flask db migrate -m "users table" >>> "this is similar to git add . & git commit -m 'note'"
$ flask db upgrade >>> "this is the equivalent of git push origin"

IF:
- you run $ flask db downgrade, you must manually DELETE the version in dir:migrations >
        dir:versions, with the old push BEFORE you re-add the change. Otherwise you will get
        an ERROR saying your target database is not up to date.

Remember that Flask-Migrate stores all Class names in snake case. If you want to
access anything after you've created a class from another class, use the snake-case name
instead of the class name.
"""

from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rolodex = db.relationship('Rolodex', backref='author', lazy='dynamic')

    # tells Python how to print objects of this class, which is useful for debugging
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Rolodex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # note that I'm using the snake-case name to access User.id
    # note that this 'many' class needs a foreign key to connect it to the 'one' class
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # useful for debugging
    def __repr__(self):
        return '<Rolodex {}>'.format(self.name)

