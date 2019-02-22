# Writeup 2 - OSINT

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (45 pts)

1. Elizabeth Moffet. I found this on her twitter account. I found that from the username tools on inteltechniques.com/

2. v0idcache works at a bank as the CEO.
	Name of Bank: Elite Banking (for the 1337 Haxor)
	URL: 1337bank.money

	email provided on the website "about": v0idcache@protonmail.com

3. Twitter account - username: v0idcache; follows UMD Cybersecurity. She is from the Netherlands. She also has a github account with the same username and she has one follower, choward4.
Her address is:
12 Leeteinde
Broek, Waterland, 1151 AK

On pastebin.com I found that there is a conversation between v0idcache and fl1nch that posted on there by a guest account.

4. LIP Address found on dnsdumpster.com: 216.87.155.33
This is one of the DNS Server IP addressed with US service (AS36619 VeriSign Global Registry

Host Record: 142.93.136.81 and is from Canada

5. From using robots.txt on the website it gives shows:
user-agent: *
Disallow: /secret_directory

Then I went to that directoy and found a flag! YAY! it said
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

This is the second flag I found:
On dnsdumpster.com in the txt section it says: "CMSC389R-{h0w_2_int0_DNS_r3c0rd5}"

6. SSH(22) and HTTP(80) are open on the website, I found this out by using the domain name search tools on inteltechniques.com. Specifically the Port Scan button under Historical data. 

The waste(1337) is also open, I did this by running the following command in my terminal:
nmap -p 1-2000 142.93.136.81

From nmap I also found three filtered ports: msrcp(135), netbios-ssn(139), and microsoftds-ds(445).

7. Ubuntu is the operating system and I found this by entering the website IP address into shodan.io.

8. None

### Part 2 (75 pts)

To find the password for the open waste port, I first ran the command "nc 142.93.136.81 1337" in my terminal to see what the port leads to and found out how the log-in for the port worked. From there I was able to figure out how to structure my code. I took the password dictionary talked about in class and read through each line of it in my script and sent in each possible password into the bruteforce method. From there I entered in the username "v0idcache" and the password to see if the credentials were correct. If they were, then I broke out of the code and printed what the password it just checked was. This got me the password "linkinpark". 

