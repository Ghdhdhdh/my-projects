import os
import sys

action=input("what do you want to do (upgrade, install see avalibale updates): ")

if action=="upgrade":
    x=input("What do you want to upgrade?")
    y='winget upgrade ' + x
    os.system(y)

if action=="install":
    x=input("What do you want to install?")
    y='winget install ' + x
    os.system(y)

if action=="see avalibale updates":

    os.system('winget upgrade')

print('done')

os.system('pause')
sys.exit
