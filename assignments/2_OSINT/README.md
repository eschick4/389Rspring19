OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1. What is `v0idcache`'s real name?

Elizabeth Moffet

2. Where does `v0idcache` work? What is the URL to their website?

She works at a bank as the CEO
Name of Bank: Elite Banking (for the 1337 Haxor)
URL: 1337bank.money

email provided on the website "about": v0idcache@protonmail.com

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.

Twitter account - username: v0idcache; follows UMD Cybersecurity;
She is from the Netherlands

She also has a github account with the same username and she has one follower choward4.

Her address is:
12 Leeteinde
Broek, Waterland, 1151 AK

On pastebin.com I found that there is a conversation between v0idcache and fl1nch. 

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

IP Address found on dnsdumpster.com: 216.87.155.33
This is one of the DNS Server IP addressed with US service (AS36619 VeriSign Global Registry

Host Record: 142.93.136.81 and is from Canada

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.

From using robots.txt on the website it gives shows:
user-agent: *
Disallow: /secret_directory

Then I went to that directoy and found a flag! YAY! it said
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

This is the second flag I found:
On dnsdumpster.com in the txt section it says: "CMSC389R-{h0w_2_int0_DNS_r3c0rd5}"

6. What ports are open on the website? What services are running behind these ports? How did you discover this?

<<<<<<< HEAD
SSH(22) and HTTP(80) are open on the website, I found this out by using the domain name search tools on inteltechniques.com. Specifically the Port Scan button under Historical data. 

The waste(1337) is also open, I did this by running the following command in my terminal:
nmap -p 1-2000 142.93.136.81

From nmap I also found three filtered ports: msrcp(135), netbios-ssn(139), microsoftds-ds(445).

7. Which operating system is running on the website? How did you discover this?
=======
7. Which operating system is running on the server that is hosting the website? How did you discover this?
>>>>>>> upstream/master

Ubuntu is the operating system and I found this by entering the website IP address into shodan.io

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)



### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
