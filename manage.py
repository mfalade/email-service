import os

from flask_script import Server, Manager

from mfalade_backend import create_app


app_env = os.environ.get('MFALADE_ENV', 'dev')
app = create_app(app_env)
port = os.environ.get('PORT', '3000')

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=port))


if __name__ == '__main__':
    manager.run()

