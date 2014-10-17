#!/usr/bin/python3 -O
# -*- coding: utf-8 -*-
import os
import sys

from criteria import *

#Définition des critères
criterias = {}
criterias["type"] 	= Criteria(0.5, [1,2], Criteria.egalize, [Criteria.exp, -1])
criterias["income"] = Criteria(0.5, [20,50], Criteria.maximize, [Criteria.exp, -1])