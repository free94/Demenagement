#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys

from criteria import *
from accomodation import *
from family import *
import math
import random

sizeMatrix = 16
sizeMaxAccomodation = 1
percentOfFamilies = 0.2
numberOfRounds = 200
firstMatrix = str()
distanceFunction = str()
function = str()
critere = str()

#TUTO COMPLET ET CLAIR POUR OPTIMISATION PYTHON : http://nliautaud.fr/wiki/articles/python_benchmark

def fcount():
	c = 0
	for a in matrix.values():
		c += len(a.listOfFamily)
	return c

def move(family):
	family.accomodation.removeFamily(family)
	scores = computeScores(family)
	# print(family.accomodation.coordinates)
	# for d in sorted(matrix.values(), key=lambda x: scores[x.coordinates], reverse=True):
	# 	print((d.coordinates, scores[d.coordinates]))
	# sys.exit()
	for destination in sorted(matrix.values(), key=lambda x: scores[x.coordinates], reverse=True):
		if(not destination.full()):
			destination.addFamily(family)
			return True
	return False

def computeScores(family):
	# score propre à un logement sans se soucier des logements voisins
	inherentScores = {}
	# print(family.accomodation.coordinates)
	for p, a in matrix.items():
		inherentScores[p] = a.getScores(family.criterias)
		# print((p, inherentScores[p]))
	# influence des logements voisins
	scores = {}
	for p1, a1 in matrix.items():
		scores[p1] = 0
		for p2, a2 in matrix.items():
			#if family.accomodation is a2:
			#	continue
			for criteria in criterias.values():
				scores[p1] += criteria.weight * inherentScores[p2][criteria] *  criteria.influence(a1.distance(a2))
		scores[p1] /= sizeMatrix ** 2
	return scores

def matrixCriteria(matrix, criteria):
	return {k : v.criteriaAveragesInAcc[criteria] for k, v in matrix.items()}

def matrixNbFamilies(matrix, criteria):
	return {k : len(v.listOfFamily) for k,v in matrix}

#------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------main----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#Définition des critères
criterias = {}
#creation d'une matrice de logements
matrix = {}
numberOfAccomodationWithFamilies = 0

def init():

	#criterias["type"] 	= Criteria(1, [1,2], Criteria.egalize, Criteria.exp)
	if(distanceFunction == "inv"):
		c = Criteria.inv
	elif(distanceFunction == "exp"):
		c = Criteria.exp
	else:
		c = Criteria.lin


	if(function == "maximize"):
		f = Criteria.maximize
	elif(function == "minimize"):
		f = Criteria.minimize
	else:
		f = Criteria.egalize

	if(critere == "income"):
		criterias["income"] = Criteria(1, [20,50], f, c)
	else:
		criterias["type"] 	= Criteria(1, [1,2], f, c)

	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			matrix[(i,j)] = Accomodation(int(random.uniform(1,sizeMaxAccomodation)), (i,j), criterias.values())

	numberOfAccomodationWithFamilies = int(percentOfFamilies * Accomodation.numberMaxOfFamilies)

	#remplissage de la matrice avec des familles : leur position est aléatoire dans la matrice
	count = 0
	while(count < numberOfAccomodationWithFamilies):
		# family = Family({criterias["income"]:int(random.uniform(20,50))},3)
		family = Family({criterias[critere]:criterias[critere].randValue()},10)
		while(True):
			i = math.floor(random.uniform(0,sizeMatrix))
			j = math.floor(random.uniform(0,sizeMatrix))
			if(matrix[(i,j)].addFamily(family)):
				family.accomodation = matrix[(i,j)]
				count += 1
				break


def round():
	l = Family.allFamilies
	random.shuffle(l)
	for f in l:
		if(f.decision()):
			move(f)
