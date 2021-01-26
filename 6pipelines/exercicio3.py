# -*- coding: utf-8 -*-

from modeller import *
from modeller.automodel import *

log.verbose()

env = environ()

env.io.atom_files_directory = ['/home/ryzen/Desktop']

env.io.hetatm = True
env.io.water = True

a = automodel(env, alnfile = 'new_alinha.pir', knows = '3UR7', sequence = 'beta_glicosidase.fasta')
a.starting_model = 1
a.ending_model = 2
a.make()