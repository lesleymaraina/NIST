from app import db

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	random = db.Column(db.Integer) 

class FormResponses(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.Integer)
	variant = db.Column(db.Integer, db.ForeignKey('variants.id'))
	q1_answer = db.Column(db.Integer, db.ForeignKey('q1_answer.id'))
	q2_answer = db.Column(db.Integer, db.ForeignKey('q2_answer.id'))
	q3_answer = db.Column(db.Integer, db.ForeignKey('q3_answer.id'))
	q4_answer = db.Column(db.String)

class q1_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	answer_choice = db.relationship('FormResponses', backref='q1_answer_ref', lazy=True)

class q2_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	answer_choice = db.relationship('FormResponses', backref='q2_answer_ref', lazy=True)

class q3_answer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	answer_text = db.Column(db.String(50))
	answer_choice = db.relationship('FormResponses', backref='q3_answer_ref', lazy=True)

class Variants(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	variant_name = db.Column(db.String(5000))
	variant_size = db.Column(db.String(100))
	variant_id = db.Column(db.String(50000)) 
	image_name = db.Column(db.String(5000)) 
	igv_image = db.Column(db.String(50000))	
	gEval_image = db.Column(db.String(50000))
	svviz_DotPlot_image = db.Column(db.String(50000))
	svviz_PB_image = db.Column(db.String(50000))
	svviz_Ill250_image = db.Column(db.String(50000))
	svviz_Ill300x_image = db.Column(db.String(50000))		
	svviz_10X_image = db.Column(db.String(50000))
	svviz_MP_image = db.Column(db.String(50000))
