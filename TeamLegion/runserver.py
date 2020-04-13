"""
This script runs the TeamLegion application using a development server.
"""

from os import environ
from TeamLegion import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '9999'))
    except ValueError:
        PORT = 9999
    app.run(HOST, PORT)
