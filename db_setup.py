# Standard Configuration for SQLAlchemy 
import sys
import os

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# End of Standard Configuration

class Creatures(Base):
	__tablename__ = 'creatures'

	id = Column(Integer, primary_key = True)
	name = Column(String(25), nullable = False)
	stamina = Column(Integer,nullable=True)
	armor = Column(Integer,nullable=True)
	damage = Column(Integer,nullable=True)
	accuracy = Column(Integer,nullable=True)
	skill = Column(Integer,nullable=True)
	strength = Column(Integer,nullable=True)
	dexterity = Column(Integer,nullable=True)
	constitution = Column(Integer,nullable=True)
	intelligence = Column(Integer,nullable=True)
	wisdom = Column(Integer,nullable=True)
	charisma = Column(Integer,nullable=True)
	vulnerabilities = Column(String(60),nullable=True)
	resistances = Column(String(60),nullable=True)
	immunities = Column(String(60),nullable=True)
	notes = Column(String(250),nullable=True)


	def __init__(self,name,stamina,armor,damage,accuracy,skill,stats,vulnerabilities='None',resistances='None',immunities='None',notes='None'):
		self.setStats(name,stamina,armor,damage,accuracy,skill,stats,vulnerabilities,resistances,immunities,notes)

	def translate(self,stat):
		if stat=='stamina':
			temp = [15,36,71,101,146,191,236]
			return temp[self.stamina-1]
		elif stat=='armor':
			temp = [8,12,14,16,18,20,22]
			return temp[self.armor-1]
		elif stat=='damage':
			temp = [6,9,21,33,51,69,87]
			return temp[self.damage-1]
		elif stat=='accuracy':
			temp =[2,4,6,8,9,10,11]
			return temp[self.accuracy-1]
		elif stat=='skill':
			temp =[2,3,4,5,6,7,9]
			return temp[self.skill-1]
		else:#skill accuracy attributes
			lookup = {'strength':self.strength,
			'dexterity':self.dexterity,
			'constitution':self.constitution,
			'intelligence':self.intelligence,
			'wisdom':self.wisdom,
			'charisma':self.charisma}
			temp =[-1,1,3,5,7,9,11]
			return temp[lookup[stat]-1]

	def _grade(self,to_grade,grades):
		if to_grade<=grades[0]:
			return 1 #F
		elif to_grade<=grades[1]:
			return 2 #D
		elif to_grade<=grades[2]:
			return 3 #C
		elif to_grade<=grades[3]:
			return 4 #B
		elif to_grade<=grades[4]:
			return 5 #A
		elif to_grade<=grades[5]:
			return 6 #S
		else:
			return 7 #SS

	def setStats(self,name,stamina,armor,damage,accuracy,skill,stats,vulnerabilities='None',resistances='None',immunities='None',notes='None'):
		self.name = name
		self.stamina = self._grade(stamina,[35,70,100,145,190,235])
		self.armor = self._grade(armor,[11,14,16,18,20,22])
		self.damage = self._grade(damage,[8,20,32,50,68,86])
		self.accuracy = self._grade(accuracy,[3,5,7,8,9,10])
		self.skill = self._grade(skill,[2,3,4,5,6,8])
		self.strength = self._grade(stats[0],[0,2,4,6,8,10])
		self.dexterity = self._grade(stats[1],[0,2,4,6,8,10])
		self.constitution = self._grade(stats[2],[0,2,4,6,8,10])
		self.intelligence = self._grade(stats[3],[0,2,4,6,8,10])
		self.wisdom = self._grade(stats[4],[0,2,4,6,8,10])
		self.charisma = self._grade(stats[5],[0,2,4,6,8,10])

		self.vulnerabilities = vulnerabilities
		self.resistances = resistances
		self.immunities = immunities
		self.notes = notes


engine = create_engine('sqlite:///radar_charts.db')

Base.metadata.create_all(engine)