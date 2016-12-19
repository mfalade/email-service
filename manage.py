"""."""
import os

from flask_script import Manager

from mfalade_backend import create_app


app_env = os.environ.get('MFALADE_ENV', 'dev')

app = create_app(app_env)

manager = Manager(app)



if __name__ == '__main__':
    manager.run()

