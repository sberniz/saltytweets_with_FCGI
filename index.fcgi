#!/home/venv/bin/python
import os
import sys

from flup.server.fcgi import WSGIServer
activate_this = '/home/venv/bin/activate_this.py'
exec(open(activate_this).read(),dict(__file__=activate_this))
info_path = '/home/www/flasktest/'
sys.path.insert(0,info_path)
os.chdir(info_path)
from flat_fcgi import app

if __name__ == '__main__':
    WSGIServer(app).run()
