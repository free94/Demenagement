#!/usr/bin/python3 -O
# -*-coding:utf-8 -*

import math

class Criteria:
	def __init__(self, weight, valuesRange, rule, influence):
		self.weight = weight
		self.valuesRange = valuesRange
		self.rule = rule # minimize, egalize, maximize
		self.influence = influence # [fonction, parametres...]

	def score(self, averageInAccomodation, valueOfFamily):
		return 1-self.rule(self, {"valueOfFamily":valueOfFamily, "averageInAccomodation":averageInAccomodation, "valuesRange":self.valuesRange})


#rules
	@staticmethod
	def egalize(cls, values):
		return math.fabs(values["valueOfFamily"] - values["averageInAccomodation"]) / (values["valuesRange"][1] - values["valuesRange"][0]) 

	@staticmethod
	def inegalize(cls, values):
		return 1-cls.egalize(values)

	@staticmethod
	def maximize(cls, values):
		return (values["valuesRange"][1] - values["valueOfFamily"]) / (values["valuesRange"][1] - values["valuesRange"][0])

	@staticmethod
	def minimize(cls, values):
		return 1-cls.maximise(values)

#influences
	@staticmethod
	def exp(cls, dec, value):
		return math.exp(dec * value)