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
sizeMaxAccomodation = 9
percentOfFamilies = 0.5
numberOfMove = 100
numberOfRounds = 2

def move(family):
	for destination in sorted(matrix.values(), key=lambda x: x.getScore(family.criterias), reverse=True):
		if(not destination.full() and destination != family.accomodation):
			#print("tuple1 : " + str(destination.coordinates) + "tuple2 : " + str(family.accomodation.coordinates))
			printMatrix(family.accomodation.coordinates, destination.coordinates)
			#printMatrixByType()
			temp = family.accomodation
			destination.addFamily(family)
			temp.removeFamily(family)

			return True
	return False

def printMatrix(tuple1, tuple2):
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if((i,j) == tuple1):
				couleur = "\033[94m" #blue = coordinates of the family
			elif((i,j) == tuple2):
				couleur = "\033[92m" #green = destination
			else:
				couleur = ""
			print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
		print("")
	print("")

def printMatrixByType():
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if(matrix[(i,j)].criteriaAveragesInAcc[criterias["type"]] > 1.5):
				couleur = "\033[94m" #blue
			else:
				couleur = "\033[92m" #green
			print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
		print("")
	print("")

#Définition des critères
criterias = {}
criterias["type"] 	= Criteria(0.5, [1,2], Criteria.egalize, [Criteria.exp, -1])
#criterias["income"] = Criteria(0.5, [20,50], Criteria.maximize, [Criteria.exp, -1])

#creation d'une matrice de logements
matrix = {}
for i in range(sizeMatrix):
	for j in range(sizeMatrix):
		matrix[(i,j)] = Accomodation(int(random.uniform(1,sizeMaxAccomodation)), (i,j), criterias.values())

numberOfAccomodationWithFamilies = int(percentOfFamilies * Accomodation.numberMaxOfFamilies)
print("\nnumberOfAccomodationWithFamilies :" + str(numberOfAccomodationWithFamilies) + "\n")

#remplissage de la matrice avec des familles : leur position est aléatoire dans la matrice
count = 0
while(count < numberOfAccomodationWithFamilies):
	family = Family({criterias["type"]:random.choice([1,2])},3)
	while(True):
		i = math.floor(random.uniform(0,sizeMatrix))
		j = math.floor(random.uniform(0,sizeMatrix))
		if	(matrix[(i,j)].addFamily(family)):
			family.accomodation = matrix[(i,j)]
			count += 1
			break

#Demande à chaque famille "rounds" fois si elle veut déménager ou pas : si oui déménagement -> move()
for i in range(numberOfRounds):
	print("-*-*-*-*-*-*-*-*-*- Rounds " + str(i+1) + " -*-*-*-*-*-*-*-*-*-\n")
	for f in Family.allFamilies:
		if(f.decision()):
			#print("famille qui veut move : " + str(f.accomodation.coordinates))
			move(f)

"""def destination():
	score = 0



	#author = Léo & Flo (Copyright 2014 all rights reserved)
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if(not matrix[(i,j)].full()):
				if(score < matrix[(i,j)].getScore(family.criterias)):
					score = matrix[(i,j)].getScore(family.criterias)


"""



