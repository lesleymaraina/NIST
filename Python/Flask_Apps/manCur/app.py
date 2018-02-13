from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SelectField
from wtforms.validators import InputRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/lmc2/manCur_Flask/manCur/db/db1.db'

db = SQLAlchemy(app)

class MyForm(FlaskForm):
	# radios = RadioField('Radios', choices=[('Homozygous Reference', 'Homozygous Reference'),('Heterozygous Variant', 'Heterozygous Variant'),('Homozygous Variant','Homozygous Variant'),('Complex [ie: 2+ variants in this region] or difficult', 'Complex [ie: 2+ variants in this region] or difficult')])
	radios = RadioField(choices=[('Homozygous Reference', 'Homozygous Reference'),('Heterozygous Variant', 'Heterozygous Variant'),('Homozygous Variant','Homozygous Variant'),('Complex [ie: 2+ variants in this region] or difficult', 'Complex [ie: 2+ variants in this region] or difficult')])
	radios2 = RadioField(choices=[('2 [most confident]', '2 [most confident]'),('1', '1'),('0 [least confident]','0 [least confident]')])
	radios3 = RadioField(choices=[('Within 10&#37; of the size of the variant', 'Within 10&#37; of the size of the variant'),('Not within 10&#37; of the size of the variant', 'Not within 10&#37; of the size of the variant'),('Unsure','Unsure')])

@app.route('/', methods=['GET', 'POST'])
def index():
	form = MyForm()
	return render_template('index.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)