#!/usr/bin/python3.4
# -*-coding:utf-8 -*

""" Classe Famille """

class family:
	"I am a family"

	#probability of the family want to move
	limit = 10;

	# Constructors
	def __init__(self):
		self.criterias = dict()

	def __init__(self, limit):
		self.criterias = dict()
		limit = limit

	def __init__(self, criterias = {}):
		self.criterias = criterias

	def __init__(self, criterias = {}, limit = 10):
		self.criterias = criterias
		limit = limit


	def printf(self):
		print("I am a family")

	def decision()
		return random.uniform(1,100) < limit

#function decision to know if the family move