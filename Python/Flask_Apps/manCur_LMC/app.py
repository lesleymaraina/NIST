from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views import *
if __name__ == '__main__':
	app.run(debug=True, port = 8080)
	# app.run(debug=True, host='0.0.0.0', port = 8080)

