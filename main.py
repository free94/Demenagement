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
	if(family.accomodation == None):
			print("whaaat")
			sys.exit(0)
	for destination in sorted(matrix.values(), key=lambda x: x.getScore(family), reverse=True):
		if(not destination.full() and destination != family.accomodation):
			print("tuple1 : " + str(destination.coordinates) + "tuple2 : " + str(family.accomodation.coordinates))
			printMatrix(family.accomodation.coordinates, destination.coordinates)
			destination.addFamily(family)
			family.accomodation.removeFamily(family)

			return True
	return False

def printMatrix(tuple1, tuple2):
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if((i,j) == tuple1):
				couleur = "\033[94m" #blue
			elif((i,j) == tuple2):
				couleur = "\033[92m" #green
			else:
				couleur = ""
			print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
		print("")
	print("")

#Définition des critères
criterias = {}
criterias["type"] 	= Criteria(0.5, [1,2], Criteria.egalize, [Criteria.exp, -1])
criterias["income"] = Criteria(0.5, [20,50], Criteria.maximize, [Criteria.exp, -1])

#creation d'une matrice 50*50 de logements
matrix = {}
for i in range(sizeMatrix):
	for j in range(sizeMatrix):
		matrix[(i,j)] = Accomodation(int(random.uniform(1,sizeMaxAccomodation)), (i,j))

numberOfAccomodationWithFamilies = int(percentOfFamilies * Accomodation.numberMaxOfFamilies)
print("numberOfAccomodationWithFamilies :" + str(numberOfAccomodationWithFamilies))

count = 0
while(count < numberOfAccomodationWithFamilies):
	family = Family(criterias["type"],3)
	while(True):
		i = math.floor(random.uniform(0,sizeMatrix))
		j = math.floor(random.uniform(0,sizeMatrix))
		if	(matrix[(i,j)].addFamily(family)):
			family.accomodation = matrix[(i,j)]
			count += 1
			break

for i in range(numberOfRounds):
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



