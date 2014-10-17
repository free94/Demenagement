#!/usr/bin/python3 -O
# -*-coding:utf-8 -*

import math

class Criteria:
	def __init__(self, weight, maxVal, rule, influence):
		self.weight = weight
		self.maxVal = maxVal
		self.rule = rule # minimize, egalize, maximize
		self.influence = influence # [fonction, parametres...]

	def score(self, averageInAccomodation, valueOfFamily):
		return 1-influence({"valueOfFamily":valueOfFamily, "averageInAccomodation":averageInAccomodation}, "maxVal":maxVal)


#rules
	@staticmethod
	def egalize(cls, values):
		return math.fabs(values["valueOfFamily"]-values["averageInAccomodation"]) / values["maxVal"]

	@staticmethod
	def inegalize(cls, values):
		return 1-math.fabs(values["valueOfFamily"]-values["averageInAccomodation"]) / values["maxVal"]

	@staticmethod
	def minimize(cls, values):
		return (values["maxVal"] - values["valueOfFamily"]) / values["maxVal"]

	@staticmethod
	def maximize(cls, values):
		return (values["valueOfFamily"] - values["maxVal"]) / values["maxVal"]

#influences
	@staticmethod
	def exp(dec, value):
		return math.exp(dec * value)