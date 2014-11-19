import argparse
import main
""" NOS PARAMETRES : 

sizeMatrix 			= Default Value 8
sizeMaxAccomodation = Default Value 5
percentOfFamilies 	= Default Value 20
sizeWindow 			= Default Value 640

"""
def parser():

	parser = argparse.ArgumentParser(description='Required parameters')

	#le simple fait d'ajouter "--" devant le nom de l'argument indique qu'il est optionnel, on ajoute alors le champ default =
	parser.add_argument('--sizeM',
						type=int, 
						action="store", 
						default=8, 
						help='an integer for the height and width of the matrix')

	parser.add_argument('--sizeAccomodation', 
						type=int, 
						action="store", 
						default=5, 
						help='Max number of family in one accomodation')

	parser.add_argument('--families',
						type = int, 
						action ="store", 
						default=20, 
						help="percentage of accomodation full of family")

	parser.add_argument('--sizeW',
						type = int, 
						action ="store", 
						default=640, 
						help="size of the window")

	parser.add_argument('--distance',
						type = str, 
						action ="store", 
						default="exp", 
						help="decreasing function : exp, lin or inv")

	args = parser.parse_args()
	return args
	#print(args.sizeW)