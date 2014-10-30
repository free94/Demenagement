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
			printMatrix(matrix, [family.accomodation.coordinates, destination.coordinates])
			#printMatrixByType()
			temp = family.accomodation
			destination.addFamily(family)
			temp.removeFamily(family)

			return True
	return False

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
	for i in range(sizeMatrix):
		for j in range(sizeMatrix):
			if(matrix[(i,j)].criteriaAveragesInAcc[criterias["type"]] > 1.5):
				couleur = "\033[94m" #blue
			else:
				couleur = "\033[92m" #green
			print(couleur + str(len(matrix[(i,j)].listOfFamily)) + "/" + str(matrix[(i,j)].maxFamily) + "\033[0m", end=' ')
		print("")
	print("")


#------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------main----------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
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

	family = Family({criterias["type"]:random.choice([1,2])},3)

	#print(matrix[(5,7)].getScore(family.criterias))
	print(matrix[(5,7)].getScoreWithDistrict(5, family.criterias, sizeMatrix, matrix))