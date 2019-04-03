# Author: Erin Schick

#!/usr/bin/env python2

import sys
import struct
import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp, = struct.unpack("<L", data[8:12])
author, = struct.unpack("8s", data[12:20])
section_count, = struct.unpack("<L", data[20:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % datetime.datetime.fromtimestamp(timestamp)) 
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % section_count)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")


offset = 24

# Loop through all sections
for x in range(0, section_count):
	# Get the section types and lengths
	stype, slen = struct.unpack("<LL", data[offset:(offset+8)])

	# Print info
	print("SECTION TYPE: %s" % hex(stype))
	print("SECTION LENGTH: %d" % int(slen))

	offset = offset + 8
	

	# ASCII
	if (int(stype) == 1):
		message, = struct.unpack("<%ds" % slen, data[offset:offset+slen])
		offset = offset + slen

		#print result
		print("ASCII MESSAGE: %s" % message)

	# UTF-8
	elif (int(stype) == 2):
		message = struct.unpack("<%dq" % temp, data[offset:offset+slen])
		offset = offset + slen

		#print result
		print("WORDS MESSAGE: %s" % message.encode('utf-8'))

	# Array of words
	elif (int(stype) == 3):
		temp = slen/8
		message = struct.unpack("<%dq" % temp, data[offset:offset+slen])
		offset = offset + slen

		#print result
		print("WORDS MESSAGE: %s" % message)

	# Array of dwords
	if (int(stype) == 4):
		for a in range(0, slen, 8):
			message, = struct.unpack("8s", data[offset+a:offset+a+8])

			#print result
			print("DOUBLES MESSAGE: %s" % message)

	# Array of doubles
	if (int(stype) == 5):
		for a in range(0, slen, 8):
			message, = struct.unpack("<d", data[offset+a:offset+a+8])

			#print result
			print("DOUBLES MESSAGE: %d" % message)

	# Cordinates
	if (int(stype) == 6):
		lat, lon = struct.unpack("<dd", data[offset:(offset+slen)])
		
		#print result
		print("CORDS MESSAGE: %d, %d" % (long(lat), long(lon)))

		offset = offset + slen


	# Reference
	if (int(stype) == 7):
		ref, = struct.unpack("<L", data[offset:(offset+slen)])
		
		#print result
		print("REFFERENCE MESSAGE: %d" % ref)

		offset = offset + slen


	# PNG 
	if (int(stype) == 8):
		png_header = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
		with open("found.png", 'wb') as f:
			f.write(png_header)
			f.write(data[offset:offset+slen])
		
		#print result
		print("THERE IS AN IMAGE HERE IT'S NAMED found.png")

		offset = offset + slen


	# GIF87
	if (int(stype) == 9):
		ref, = struct.unpack("<%ds" % slen, data[offset:offset+slen])
		file = open("found87.gif87", "w")
		file.write(gif87)
		file.close()

		#print result
		print("THERE IS AN GIF HERE IT'S NAMED found87.gif87")

		offset = offset + slen


	# GIF89
	if (int(stype) == 10):
		ref, = struct.unpack("<%ds" % slen, data[offset:offset+slen])
		file = open("found89.gif89", "w")
		file.write(gif89)
		file.close()

		#print result
		print("THERE IS AN GIF HERE IT'S NAMED found89.gif89")

		offset = offset + slen


print("********* END ***************")















