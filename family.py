#!/usr/bin/python3.4
# -*-coding:utf-8 -*
from random import *

""" Classe Famille """

class Family:
	"I am a family"

	#probability of the family want to move
	limit = 10
	allFamilies = list()
	# Constructor
	def __init__(self, criterias, limit):
		self.criterias = criterias
		Family.allFamilies.append(self)
		Family.limit = limit
		self.accomodation = None

	def decision(self):
		return uniform(1,100) < Family.limit

#function decision to know if the family move