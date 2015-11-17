#!/usr/bin/env python

from time import sleep
from os import system

# okay, so... let's make a small box
def makebox():
	print '+' * 80
	for i in range(25):
		print '+' + ' '*78 + '+'
		sleep(0.1)
	print '+' * 80

system('clear')
makebox()