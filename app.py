from db_setup import *
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash
from flask import session as login_session
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, exc

import os
import random
import string

engine = create_engine('sqlite:///radar_charts.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)

from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,IntegerField,TextAreaField
from wtforms.validators import DataRequired

class selectMon(FlaskForm):
	mon1 = SelectField('mon1',coerce=int)
class createMon(FlaskForm):
	name = StringField('name')
	stamina = IntegerField('stamina')
	armor = IntegerField('armor')
	skill = IntegerField('skill')
	accuracy = IntegerField('accuracy')
	damage = IntegerField('damage')
	strength = IntegerField('strength')
	dexterity = IntegerField('dexterity')
	constitution = IntegerField('constitution')
	intelligence = IntegerField('intelligence')
	wisdom = IntegerField('wisdom')
	charisma = IntegerField('charisma')
	vulnerabilities = StringField('vulnerabilities')
	resistances = StringField('resistances')
	immunities = StringField('immunities')
	notes = StringField('notes')

@app.route('/',methods=['POST','GET'])
def index():
	form = selectMon()
	creatures = session.query(Creatures)
	creature = creatures.first()
	form.mon1.choices=[(c.id,c.name) for c in creatures.all()]

	if form.validate_on_submit():
		creature = creatures.filter_by(id=form.mon1.data).first()

	return render_template('index.html', form=form, creature=creature)

@app.route('/new',methods=['POST','GET'])
def new():
	form = createMon()
	if form.validate_on_submit():
		creature = Creatures(form.name.data,form.stamina.data,form.armor.data,form.damage.data,
			form.accuracy.data,form.skill.data,
			[form.strength.data,form.dexterity.data,form.constitution.data,
			form.intelligence.data,form.wisdom.data,form.charisma.data],
			form.vulnerabilities.data,form.resistances.data,form.immunities.data,form.notes.data)
		try:
			session.add(creature)
			session.commit()
			return redirect(url_for('.index'))
		except exc.IntegrityError:
			session.rollback()
			return render_template('form.html', form=form, error=str(sys.exc_info()[1]).split(") ")[1].split(" [")[0])

	return render_template('form.html', form=form)

@app.route('/edit/<mon>',methods=['POST','GET'])
def edit(mon):
	creatures = session.query(Creatures)
	creature = creatures.filter_by(id=mon).first()
	form = createMon()
	if form.validate_on_submit():
		creature.setStats(form.name.data,form.stamina.data,form.armor.data,form.damage.data,
			form.accuracy.data,form.skill.data,
			[form.strength.data,form.dexterity.data,form.constitution.data,
			form.intelligence.data,form.wisdom.data,form.charisma.data],
			form.vulnerabilities.data,form.resistances.data,form.immunities.data,form.notes.data)
		try:
			session.add(creature)
			session.commit()
			return redirect(url_for('.index'))
		except exc.IntegrityError:
			session.rollback()
			return render_template('form.html', form=form, creature=creature, error=str(sys.exc_info()[1]).split(") ")[1].split(" [")[0])
	return render_template('form.html', form=form, creature=creature)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0',port=5000)