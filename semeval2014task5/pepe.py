#Code to generate the evaluation output seen here

import libsemeval2014task5
import matplotlib.pyplot as plt
import glob
import os
import numpy as np
from IPython.display import HTML

DIR = "/home/migue/Desktop/TTT/semeval2014task5/evaluation/"
os.chdir(DIR)

def evaluate():
    for f in sorted(glob.glob('*xml')):
        if f.find('matrex') != -1:
            #skip intermediate files
            continue
        fields = os.path.basename(f).split('.')
        team = fields[0]
        L1, L2 = fields[1].split('-')
        run = fields[2]

        #Find evaluation type, can be best or oof
        #If not specified, the file will be evaluated according to both metrics
        if fields[3] == 'xml':
            eval = 'both'
        else:
            eval = fields[3]

        if eval == 'both' or eval == 'best':
            #BEST Evaluation
            print("Processing " + f  + " (BEST)")
            if eval == 'both':
                evalf = team + '.' + L1 + '-' + L2 + '.' + run + '.best.xml'
                os.rename(f, evalf) #temporary rename so output files will be consistently named
            else:
                evalf = f
            cmd = "semeval2014task5-evaluate -I --ref ../corpus/" + \
            L1 + "-" + L2 + ".gold.tokenised.xml --out " + evalf + "> " + evalf.replace('.xml','.log') + " 2> /dev/null"
            print cmd
            r = os.system(cmd)
            if eval == 'both':
                os.rename(evalf, f) #undo temporary rename
            if r != 0:
                print("Failed prematurely!")
                return
        if eval == 'both' or eval == 'oof':
            #OOF Evaluation
            print("Processing " + f  + " (OOF)")
            if eval == 'both':
                evalf = team + '.' + L1 + '-' + L2 + '.' + run + '.oof.xml'
                os.rename(f, evalf)  #temporary rename so output files will be consistently named
            else:
                evalf = f
            cmd = "semeval2014task5-evaluate -I -a --ref ../corpus/" + \
            L1 + "-" + L2 + ".gold.tokenised.xml --out " + evalf + "> " + evalf.replace('.xml','.log') + " 2> /dev/null"
            print
            print cmd
            r = os.system(cmd)
            if eval == 'both':
                os.rename(evalf, f) #undo temporary rename
            if r != 0:
                print("Failed prematurely!2")
                return
    print("Done")


evaluate()

data = {}
