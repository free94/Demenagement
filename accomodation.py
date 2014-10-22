#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys
from random import *
from criteria import *
	
class Accomodation :

	#global number of accomodation
	numberMaxOfFamilies = 0

	def __init__(self, maxF, coordinates): # Notre methode constructeur

		#nombre total d'accomodations - static
		Accomodation.numberMaxOfFamilies += maxF
		#entier indiquant le nombre max de familles pouvant cohabiter dans ce logement
		self.maxFamily = maxF
		#liste contenant la ou les familles presentes dans ce logement
		self.listOfFamily = list()
		#dictionnaire des criteres : suffira de faire criterias["monCritere"] = ...
		self.criterias = dict()
		self.coordinates = coordinates

	def addFamily(self, family):
		if(self.maxFamily > len(self.listOfFamily)):
			family.accomodation = self
			self.listOfFamily.append(family)
			return True
		else:
			return False

	def removeFamily(self, family):
		try:
			self.listOfFamily.remove(family)
			return True
		except Exception as e:
			print ("impossible de supprimer l'element "+ str(family) +"de la liste" + str(e))
			return False		

	#récupération du "score" qu'obtient un logement au vu des criteres d'une famille souhaitant s'y installer		

	"""Principe"""
	"""
	SCORE DU LOGEMENT

	-Calcul des moyennes PAR CRITERE des valeurs des criteres des differentes familles du logement
	-Appel de la fonction score() de la classe Criteria multiplie a critere.ponderation :
		SOMME(critere.ponderation x critere.score(moyenne, val)) pour chaque critere
	-Return le score

	--> Que calcul critere.score(moyenne,val) : un score fonction de la demande de la famille (minimiser, maximiser, trouver le res le + proche etc)

	SCORE VOISINNAGE

	-Ajout au score du logement de ponderation*logementVoisin : ponderation dependant de la distance entre logement et voisin

	"""
	def getScore(self, familyCriterias):
		finalScore = 0
		averageByCriteria = dict()
		i = 0

		#Calcul de la moyenne par critere
		for family in self.listOfFamily:
			i+=1
			#parcours de l'ensemble des cles du dictionnaire et de leur valeur
			for key, value in self.criterias.items():
				averageByCriteria[key] = ( averageByCriteria[key] + value )
		
		#calcul du score final en appelant pour chaque critere la fonction score DANS critere
		for criteria, value in self.criterias:
			averageByCriteria[criteria] = averageByCriteria[criteria] / i
			finalScore += criteria.weight * criteria.score(averageByCriteria[criteria], value)	
		
		return finalScore

	def full(self):
		return self.maxFamily == len(self.listOfFamily)

