import argparse
import shutil
import os
import subprocess as sp
from udacity_pa import udacity

nanodegree = 'nd889'
projects = ['rnn']
filenames = ['my_answers.py', 'RNN_project.ipynb', 'RNN_project.html']

def submit(args):

  sp.call(['jupyter', 'nbconvert', '--to', 'html', 'RNN_project.ipynb'])

  udacity.submit(nanodegree, projects[0], filenames, 
                 environment = args.environment,
                 jwt_path = args.jwt_path)
