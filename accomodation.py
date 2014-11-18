#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys
import math
from main import *
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
			self.criteriaAveragesInAcc[criteria] = None
		#coordonnées du logement sur la grille
		self.coordinates = coordinates

	def addFamily(self, family):
		if(self.maxFamily > len(self.listOfFamily)):
			family.accomodation = self
			self.listOfFamily.append(family)
			self.addInAverage(family)
			return True
		else:
			return False

	def removeFamily(self, family):
		try:
			self.listOfFamily.remove(family)
			self.removeInAverage(family)
			return True
		except Exception as e:
			print ("impossible de supprimer l'element "+ str(family) +"de la liste -> " + str(e))
			return False

	def addInAverage(self, family):
		self.criteriaAveragesInAcc = { c : ((0 if a is None else a)*(len(self.listOfFamily)-1) + family.criterias[c]) / len(self.listOfFamily) for c,a in self.criteriaAveragesInAcc.items()}

	def removeInAverage(self, family):
		if not self.empty():
			self.criteriaAveragesInAcc = { c : (a *(len(self.listOfFamily)-1) - family.criterias[c]) / len(self.listOfFamily) for c,a in self.criteriaAveragesInAcc.items()}
		else:
			self.criteriaAveragesInAcc = { c : None for c in self.criteriaAveragesInAcc.keys() }

	#mise à jour des valeurs moyennes des critères pour le logement.
	def updateAverages(self):
		for criteria in self.criteriaAveragesInAcc.keys():
			self.criteriaAveragesInAcc[criteria] = 0

		#si le logement est vide : 0 famille, on décide de laisser à zéro les moyennes des critères du logement, sinon on maj
		if(len(self.listOfFamily) > 0) :
			for family in self.listOfFamily:
				for criteria in self.criteriaAveragesInAcc.keys():
					self.criteriaAveragesInAcc[criteria] += family.criterias[criteria]

			for criteria in self.criteriaAveragesInAcc.keys():
				self.criteriaAveragesInAcc[criteria] = self.criteriaAveragesInAcc[criteria] / len(self.listOfFamily)

	#score de l'immeuble selon ses valeurs moyennes de critères et les valeurs de la famille qui veut y emmenager

	def getScores(self, familyValues):
		scores = {}
		for criteria in self.criteriaAveragesInAcc.keys():
			scores[criteria] = criteria.score(self.criteriaAveragesInAcc[criteria], familyValues[criteria])
		return scores

	def getMyScores(self, familyValues):
		scores = {}
		for criteria in self.criteriaAveragesInAcc.keys():
			if len(self.listOfFamily) - 1 > 0:
				value = (self.criteriaAveragesInAcc[criteria] * (len(self.listOfFamily)) - familyValues[criteria]) / (len(self.listOfFamily) - 1)
				scores[criteria] = criteria.score(value, familyValues[criteria])
			else:
				scores[criteria] = None
		return scores

	#score de l'immeuble ajusté par celui de ses voisins
	"""def getScoreWithDistrict(self, distanceLimit, familyValues, sizeMatrix, matrix):
		score = 0
		placeInTheDistrict = list()
		for i in range(sizeMatrix):
			for j in range(sizeMatrix):
				if(self.distance(matrix[(i,j)]) < distanceLimit and matrix[(i,j)] != self):
					score += matrix[(i,j)].getScore(familyValues, matrix[(i,j)]) * (1 / self.distance(matrix[(i,j)]))
					placeInTheDistrict.append((i,j))
		print("****************************")
		printMatrix(matrix, placeInTheDistrict)
		print("****************************")
		return score
		"""
	def full(self):
		return self.maxFamily == len(self.listOfFamily)

	def empty(self):
		return not self.listOfFamily

	#retourne la distance entre self et l'accomodation en parametre
	def distance(self, accomodation):
		return math.fabs(self.coordinates[0] - accomodation.coordinates[0]) + math.fabs(self.coordinates[1] - accomodation.coordinates[1])
