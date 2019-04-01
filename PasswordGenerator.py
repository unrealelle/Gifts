# File: randpassgen.py

import secrets

# Get number of password characters and number of sequences
while True:
	try:
		num_chars = int(input('\nEnter number of password characters: '))
		break
	except ValueError:
		pass

while True:
	try:
		num_seqs = int(input('Enter desired iterations: '))
		break
	except ValueError:
		pass

print() # some white space

# Get a list of the printable ascii characters
ascii_list = []
for i in range(33, 127): # ascii 33-126
	ascii_list.append(chr(i)) # chr(i) gets ascii character by decimal number

# Generate desired number of password sequences of desired length
for i in range(0, num_seqs):
	password = []
	for i in range(0, num_chars):
		password.append(secrets.choice(ascii_list))

	password = ''.join(password) # Convert char list to a string
	print(password)

print() # some white space
