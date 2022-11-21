#IMPORTING THE NEEDED MODULES

import urllib.request as ur
import numpy as np
import pymatgen.io.cif   # this help us query the MP database
from pymatgen.ext.matproj import MPRester
from pymatgen.ext.matproj import MPRestError

m = MPRester("Jbm6FXHA5AyIqvS1ZXJ2bxmEPMhRBed5")


#GETTING AND CONVERTING OUR FILE
file_url = "https://drive.google.com/file/d/1jT1EtNEPFlIYxsFNTbtdxzPlV9foMhKv/view?usp=share_link"
opfile = ur.urlopen(file_url)

CifFile = opfile.read().decode('utf-8')# this reads the file
parser = .pymatgen.io.cif.CifParser.from_string(CifFile)# this converts the file into a String data



#METHODS FOR ACCESING SOME UNIQUE FEATURES OF OUR STRUCTURE

structure = parser.get_structures() # returns list of structure objects

#print(structure[0])

#structure = structure[0]

#print(structure.lattice)
#print(structure.species)
#print(structure.charge)
#print(structure.cart_coords)
#print(structure.atomic_numbers)
#print(structure.distance_matrix)


#MAKING A DESCRIPTOR EXTRACTOR

#structure = structure[0]
#mean_atomic_number = np.mean(structure.atomic_numbers)
#max_atomic_number = np.max(structure.atomic_numbers)
#min_atomic_number = np.min(structure.atomic_numbers)
#std_atomic_numbers = np.std(structure.atomic_numbers)

#print(mean_atomic_number,max_atomic_number,min_atomic_number,max_atomic_number,std_atomic_numbers)


