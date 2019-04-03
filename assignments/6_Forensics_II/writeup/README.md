# Writeup 6 - Forensics

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (45 Pts)

1) IP address 159.203.113.181 was attacked (was the Destination)

2) The attacker probably used nmap or the domain name search tools on inteltechniques.com (specifically the Port Scan button under Historical data) to get the different port numbers that they were scanning through.

3) IP address 142.93.136.81 was the attacker and they are connected from an ethernet source.

4) They are using port #21 on the victim's server and #55914 on the attacker's server

5) use exif on image
	a) It's a jpeg file called find_me.jpeg
	
	b) This photo was taken in Punta Del Este, Urguay. I don't think this was take from a building but if you enter in the coordinates into google maps you get this pinpoint "Rambla General Jose Artigas, 20100 Punta del Este, Departamento de Maldonado, Uruguay".
	
	c) The Creation Date is: 2018:12:23 17:16:24
	
	d) An iPhone 8 took this photo
	
	e) The altitude the photo was taken at was 4.5m below sea level

6) The attacker left the file greetz.fpff on the server.

7) Making a stronger password for the ports so that the attacker cannot log in. From then also possibly using two forms of verification for all ports.


### Part 2 (55 Pts)

*** Ran everything with: python stub.py raw_greetz.fpff

1) When was it generated: 2019-03-27 00:15:05

2) Author: fl1nch

3) Here are the 5 sections:

	a) Type: Section_ASCII Length: 24 bytes Message: Hey you, keep looking :)
	b) Type: Section_Coord Length: 16 Coord: 52, 4
	c) Type: Section_PNG Length: 202776 Picture: ** will be in writeup folder **
	d) Type: Section_ASCII Length: 44 bytes Message: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC
	e) Type: Section_ASCII Length: 80 bytes Message: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

4) Flag: CMSC398R-{h0pefully_y0u_didnt_grep_CMSC389R} and CMSC398R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}

