#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys
from random import *
from criteria import *
	
class Accomodation :

	#global number of accomodation
	numberMaxOfFamilies = 0

	def __init__(self, maxF, coordinates, criterias): # Notre methode constructeur

		#nombre total d'accomodations - static
		Accomodation.numberMaxOfFamilies += maxF
		#entier indiquant le nombre max de familles pouvant cohabiter dans ce logement
		self.maxFamily = maxF
		#liste contenant la ou les familles presentes dans ce logement
		self.listOfFamily = list()
		#dictionnaire associant à chaque critère la moyenne des valeurs des familles du logement
		self.criteriaAveragesInAcc = {}
		for criteria in criterias:
			self.criteriaAveragesInAcc[criteria] = 0
		#coordonnées du logement sur la grille
		self.coordinates = coordinates

	def addFamily(self, family):
		if(self.maxFamily > len(self.listOfFamily)):
			family.accomodation = self
			self.listOfFamily.append(family)
			self.updateAverages()
			return True
		else:
			return False

	def removeFamily(self, family):
		try:
			self.listOfFamily.remove(family)
			self.updateAverages()
			return True
		except Exception as e:
			print ("impossible de supprimer l'element "+ str(family) +"de la liste" + str(e))
			return False

	#mise à jour des valeurs moyennes des critères pour le logement.
	def updateAverages(self):
		for criteria in self.criteriaAveragesInAcc.keys():
			self.criteriaAveragesInAcc[criteria] = 0

		for family in self.listOfFamily:
			for criteria in self.criteriaAveragesInAcc.keys():
				self.criteriaAveragesInAcc[criteria] += family.criterias[criteria]

		for criteria in self.criteriaAveragesInAcc.keys():
			self.criteriaAveragesInAcc[criteria] = self.criteriaAveragesInAcc[criteria] / len(self.listOfFamily)

	#score de l'immeuble selon ses valeurs moyennes de critères et les valeurs de la famille qui veut y emmenager
	def getScore(self, familyValues):
		score = 0
		for criteria in self.criteriaAveragesInAcc.keys():
			score += criteria.weight * criteria.score(self.criteriaAveragesInAcc[criteria], familyValues[criteria])
		return score


	def full(self):
		return self.maxFamily == len(self.listOfFamily)