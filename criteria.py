#!/usr/bin/python3 -O
# -*-coding:utf-8 -*

import math

class Criteria:
	def __init__(self, weight, valuesRange, rule, influence):
		self.weight = weight
		self.valuesRange = valuesRange
		self.rule = rule # minimize, egalize, maximize
		self.influence = influence #fonction

	def score(self, averageInAccomodation, valueOfFamily):
		return 1-self.rule({"valueOfFamily":valueOfFamily, "averageInAccomodation":averageInAccomodation, "valuesRange":self.valuesRange})


#rules
	@staticmethod
	def egalize(values):
		return math.fabs(values["valueOfFamily"] - values["averageInAccomodation"]) / (values["valuesRange"][1] - values["valuesRange"][0]) 

	@staticmethod
	def inegalize(values):
		return 1-cls.egalize(values)

	@staticmethod
	def maximize(values):
		return (values["valuesRange"][1] - values["valueOfFamily"]) / (values["valuesRange"][1] - values["valuesRange"][0])

	@staticmethod
	def minimize(values):
		return 1-cls.maximise(values)

#influences
	@staticmethod
	def exp(distance):
		return math.exp(-distance)