from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired
from flask_boostrap import Bootstrap


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/lmc2/manCur_Flask/manCur/db/db1.db'

db = SQLAlchemy(app)

class MyForm(FlaskForm):
	radios = RadioField('Radios', choices=[('Homozygous Reference', 'Homozygous Reference'),('Heterozygous Variant', 'Heterozygous Variant'),('Homozygous Variant','Homozygous Variant'),('Complex [ie: 2+ variants in this region] or difficult', 'Complex [ie: 2+ variants in this region] or difficult')])

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)