#!/usr/bin/env python

from os import environ
import subprocess

from flask.ext.script import Manager
from urlobject import URLObject

# initialize app before further imports
from application import initialize_app
from application import settings
app = initialize_app(settings)

from application.models import db

manager = Manager(app)

DATABASE_URL = URLObject(environ['DATABASE_URL'])

@manager.command
def recreatedb():
    "dropdb, createdb and sync scheme"
    database_name = DATABASE_URL.path[1:]
    try:
        subprocess.check_call(['dropdb', database_name])
        subprocess.check_call(['createdb', database_name])
    except subprocess.CalledProcessError, error:
        return error.returncode
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    manager.run()
