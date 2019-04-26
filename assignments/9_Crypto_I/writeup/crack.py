#!/usr/bin/env python3

import hashlib
import string

def crack():
	with open('hashes.txt') as h:
		hashes = h.read().split("\n")[:-1]
	#hashes = open('hashes.txt', 'r')
	with open('passwords.txt') as p:
		passwords = p.read().split('\r\n')[:-1]


	#passwords = open('passwords.txt', 'r')
	characters = string.ascii_lowercase

	#print("got into method")

	# Somehow it is going through every character but not every password for each character

	for c in characters:
		for p in passwords:
			for h in hashes:
				val = (c + p).strip()
				createdhash = hashlib.sha256(val.encode()).hexdigest()
				if createdhash == h:
				    print("Got into the if statement")
	           		    print(val + ": " + createdhash + "\n")

if __name__ == "__main__":
	crack()
