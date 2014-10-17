#!/usr/bin/python3
# -*-coding:utf-8 -*

class Criteria:
	__init__(self, weighting, values, rule, influence):
		self.weighting = weighting
		self.values = values # [vmin]
		self.rule = rule # min, =, max
		self.influence = influence