#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys

from criteria import *
from accomodation import *
from family import *
from functools import cmp_to_key
import math
import random

sizeMatrix = 10
sizeMaxAccomodation = 5
percentOfFamilies = 0.2
numberOfRounds = 200
firstMatrix = str()

def move(family):
	scores = computeScores(family.criterias)
	for destination in sorted(matrix.values(), key=lambda x: scores[x.coordinates], reverse=True):
		if(not destination.full()):
			if(destination != family.accomodation):
				temp = family.accomodation
				destination.addFamily(family)
				temp.removeFamily(family)

			return True
	return False

def computeScores(familyValues):
	# score propre à un logement sans se soucier des logements voisins
	inherentScores = {}
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			inherentScores[(i,j)] = matrix[(i,j)].getScore(familyValues, matrix[(i,j)])
	# influence des logements voisins
	influencedScores = {}
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			influencedScores[(i,j)] = 0
			for i2 in range(sizeMatrix):
				for j2 in range(sizeMatrix):
					if((i,j) != (i2,j2)):
						influencedScores[(i,j)] += matrix[(i,j)].getScore(familyValues, matrix[(i2,j2)])
			influencedScores[(i,j)] /= (sizeMatrix ** 2 - 1)
	# score prenant en compte le score du logement et l'influence des logements voisins
	res = {}
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			res[(i,j)] = inherentScores[(i,j)] + influencedScores[(i,j)]
	return res

def matrixCriteria(matrix, criteria):
	return {k : v.criteriaAveragesInAcc[criteria] for k, v in matrix.items()}

def matrixNbFamilies(matrix, criteria):
	return {k : len(v.listOfFamily) for k,v in matrix}


#affichage matrice avec mise en relief des n tuples de la liste
def printMatrix(matrix, listTuple):
	#S'il n'y a que deux tuples à mettre en relief on est dans le cas : départ - destination -> 2 couleurs differentes
	if(len(listTuple) == 2):
		for i in range(sizeMatrix):
			for j in range(sizeMatrix):
				if((i,j) == listTuple[0]):
					couleur = "\033[94m" #blue = coordinates of the family
				elif((i,j) == listTuple[1]):
					couleur = "\033[92m" #green = destination
				else:
					couleur = ""
				print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
			print("")
		print("")
	#Si on a + de 2 tuples a mettre en valeur par la couleur, on affiche tous ces tuples d'une couleur particuliere sans distinction
	elif(len(listTuple) > 2):
		for i in range(sizeMatrix):
			for j in range(sizeMatrix):
				if((i,j) in listTuple):
					couleur = "\033[94m" #red = coordinates of one of the families to print
				else:
					couleur = ""
				print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
			print("")
		print("")


def printMatrixByType():
	first = False
	#si c'est la première matrice
	global firstMatrix
	if(not firstMatrix):
		first = True
		firstMatrix += "\n**********The first matrix was **********\n\n"
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if(len(matrix[(i,j)].listOfFamily) == 0):
				couleur = "\033[0m" #defautl color
			elif(matrix[(i,j)].criteriaAveragesInAcc[criterias["type"]] > 1.5):
				couleur = "\033[94m" #blue
			else:
				couleur = "\033[92m" #green
			print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
			if(first):
					firstMatrix += couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m" + " "
		print("")
		if(first):
			firstMatrix += "\n"
	print("")



#------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------main----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#Définition des critères
criterias = {}
#creation d'une matrice de logements
matrix = {}
numberOfAccomodationWithFamilies = 0

def init():

	criterias["type"] 	= Criteria(1, [1,2], Criteria.egalize, Criteria.exp)
	# criterias["income"] = Criteria(0.5, [20,50], Criteria.egalize, Criteria.exp)

	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			matrix[(i,j)] = Accomodation(int(random.uniform(1,sizeMaxAccomodation)), (i,j), criterias.values())

	numberOfAccomodationWithFamilies = int(percentOfFamilies * Accomodation.numberMaxOfFamilies)

	#remplissage de la matrice avec des familles : leur position est aléatoire dans la matrice
	count = 0
	while(count < numberOfAccomodationWithFamilies):
		# family = Family({criterias["income"]:int(random.uniform(20,50))},3)
		family = Family({criterias["type"]:int(random.choice([-1, 1]))},3)
		while(True):
			i = math.floor(random.uniform(0,sizeMatrix))
			j = math.floor(random.uniform(0,sizeMatrix))
			if(matrix[(i,j)].addFamily(family)):
				family.accomodation = matrix[(i,j)]
				count += 1
				break


def round():
		for f in Family.allFamilies:
			if(f.decision()):
				move(f)
