#!/usr/bin/python3 -O
# -*-coding:utf-8 -*

import math
import random

class Criteria:
	def __init__(self, weight, valuesRange, rule, influence):
		self.weight = weight
		self.valuesRange = valuesRange
		self.average = (valuesRange[1] + valuesRange[0]) / 2
		self.rule = rule # minimize, egalize, maximize
		self.influence = influence #fonction

	def score(self, averageInAccomodation, valueOfFamily):
		return 1-self.rule({"valueOfFamily":valueOfFamily, "averageInAccomodation":averageInAccomodation, "valuesRange":self.valuesRange})

	def randValue(self):
		return random.randint(self.valuesRange[0], self.valuesRange[1])


#rules
	@staticmethod
	def egalize(values):
		return math.fabs(values["valueOfFamily"] - values["averageInAccomodation"]) / (values["valuesRange"][1] - values["valuesRange"][0])

	@staticmethod
	def inegalize(values):
		return 1-Criteria.egalize(values)

	@staticmethod
	def maximize(values):
		return (values["valuesRange"][1] - values["valueOfFamily"]) / (values["valuesRange"][1] - values["valuesRange"][0])

	@staticmethod
	def minimize(values):
		return 1-Criteria.maximize(values)

#influences
	@staticmethod
	def exp(distance):
		return math.exp(-distance)
	@staticmethod
	def lin(distance):
		return (-distance)
	@staticmethod
	def inv(distance):
		if(distance > 0):
			return 1/distance
		else:
			return 1
