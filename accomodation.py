""" Class Accomodation """

#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys
import random

#Collection <Famille>
#Nombre max de familles
#HashMap <critere, valeur>

class Accomodation :

	#global number of accomodation
	numberOfAccomodation = 0 

	def __init__(self, maxF): # Notre methode constructeur

		#nombre total d'accomodations - static
		numberOfAccomodation += 1
		#entier indiquant le nombre max de familles pouvant cohabiter dans ce logement
		self.maxFamily = maxF
		#liste contenant la ou les familles presentes dans ce logement
		self.listOfFamily = list()
		#dictionnaire des criteres : suffira de faire criterias["monCritere"] = ...
		self.criterias = dict()

	def addFamily(family):
		if(maxFamily > self.listOfFamily.__len__()):
			self.listOfFamily.append(family)
			return True
		else:
			return False

	def getWeight():
		weight = 0
		#parcours de l'ensemble des cles du dictionnaire et de leur valeur
		for key, value in self.criterias.items():
			#traitement
			weight += value
		return weight