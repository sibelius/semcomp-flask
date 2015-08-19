#!/usr/bin/env python
import os
from semcomp import create_app, db
from flask.ext.script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.use_reloader = True
app.debug = True

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(port=5000, host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
