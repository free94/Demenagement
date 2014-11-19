import argparse
import main
""" NOS PARAMETRES : 

sizeMatrix 			= Default Value 8
sizeMaxAccomodation = Default Value 5
percentOfFamilies 	= Default Value 20
sizeWindow 			= Default Value 640

"""
def parser():

	parser = argparse.ArgumentParser(description='Optional parameters')

	#le simple fait d'ajouter "--" devant le nom de l'argument indique qu'il est optionnel, on ajoute alors le champ default =
	parser.add_argument('--sizeM',
						type=int, 
						action="store", 
						default=8, 
						help='Integer for the height and width of the matrix')

	parser.add_argument('--sizeA', 
						type=int, 
						action="store", 
						default=5, 
						help='Max number of family in one accomodation')

	parser.add_argument('--families',
						type = int, 
						action ="store", 
						default=20, 
						help="Percentage of accomodation with family")

	parser.add_argument('--sizeW',
						type = int, 
						action ="store", 
						default=640, 
						help="Size of the window")

	parser.add_argument('--distance',
						type = str, 
						action ="store", 
						default="exp", 
						help="Decreasing function of distance impact: exp, lin or inv")

	parser.add_argument('--function',
						type = str, 
						action ="store", 
						default="egalize", 
						help="Possible values : maximize, minimize, egalize")

	parser.add_argument('--criteria',
						type = str, 
						action ="store", 
						default="income", 
						help="income or type")

	args = parser.parse_args()
	return args
	#print(args.sizeW)