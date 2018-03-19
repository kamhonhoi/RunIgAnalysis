#!/usr/bin/python

# Kam Hon Hoi
# 03/19/2018

# This script is to accompany the docker image kamhonhoi/iganalysis:1.0 to run the analysis pipeline
# Requirement: Create working folder in the Desktop folder

# Usage: python RunIgAnalysis.py

import os

dockercmd="sudo docker run -i --rm --user iganalysis -v ~/Desktop/working:/home/iganalysis/IgAnalysis/working -w /home/iganalysis/IgAnalysis kamhonhoi/iganalysis:1.0 /bin/bash -c "

antigen=raw_input("Antigen: ")
platform=raw_input("Platform: ")
chain=raw_input("Chain (VH or VK): ").upper()
species=raw_input("Species: ").lower()
motifspecies=species[0].upper()+species[1:]
filename=raw_input("Input filename: ")

dockercmd=dockercmd+("'python IgAnalysis_Workflow.py -a %s -p %s -c %s -cm %s -cdr %s -s %s working/%s'"%(antigen,platform,chain,motifspecies,motifspecies,species,filename))

os.system(dockercmd)


