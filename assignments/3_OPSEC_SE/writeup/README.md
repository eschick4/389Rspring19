# Writeup 3 - Operational Security and Social Engineering

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (40 pts)

For this I would pretend that I'm a person that works for the security company for the bank and say that we are getting only black footage from the bank's security cameras and we need Elizabeth's help to troubleshoot the problem so that we can make sure her bank stays secure. To get her mother's maiden name I would say that it's a security measure for our company to know that we are really talking to Elizabeth Moffet that we need to ask you a question to verify your identity. Then I would ask for her mother's maiden name as the identifying question. I would get the browser name by giving her a fake website to visit that sounds like it would be a website that would connect to the cameras in the building to show the feed and when the website says not found I would say something like "What browser are you using because sometimes the website has trouble loading on some browsers". Most likely this is the browser she normally uses if I just say "would you be able to go to this URL for me". To get the town she was born in I would do something like mention her accent and ask her where she is from. If the answer is too general I would ask for something more specific because "wow that's so weird my sister just moved there". That would make more of a personal connection to Elizabeth and would allow me to figure out that piece of information. Then I could probably mention all the pets that my sister has in her new place and ask her if she's had any pets as a kid or now. I would try to make this sound normal by saying that there is a test running/compiling now but I still need her to stay on the line in case we need more information. I would probably then start talking about my first pet and how much I loved it (fake story of course). Then as her how she got her first pet. Then I would probably be able to ask the name of the pet if it wasn't in the story of how she got her first pet by saying something like "that's such a cute story what was it's name, I'm sure it is equally as cute". After that I would pretend that we were getting closer to figuring out the problem and probably ramble off some technical terms so she thinks I know what I am talking about. Then I would say okay, "so we are close but on my end it's asking for a pin number and we don't have one on file for you, this was most likely lost in our company's move to a different office building because I've had the same issue with some other clients this week too. Do you know what this would be, maybe a ATM pin number?" After all of this, I would say that we found the bug and that we are on the job to make sure the security cameras are back up on our end so we can continue monitoring the bank correctly. 

### Part 2 (60 pts)

1. Stronger passwords: The passwords that Elizabeth was using were too weak and could be found easily. The longer the password, the better. I would recommend from research that she has a password that is at least 12 characters long and is able to copy and paste her password into the password box. I recommend that Elizabeth doesn't make a password based on personal information. She should try to make it random in order to make it harder for a hacker to use social engineering to get into your system. There should also be a combination of numbers and symbols in your password to make it more complex. Also, try not to replace letters with numbers that are similar, for example 1 for l or 3 for e. Finally, make sure that you have a different password for different accounts throughout your company. Ideally, a password that abides by the NIST guidelines is ideal. 

Sources: https://www.sagedatasecurity.com/blog/what-makes-a-strong-password-and-six-steps-to-create-one/
		 https://spycloud.com/new-nist-guidelines/

2. Searchable directories: If you are trying to keep something private on the web server, then you don't want it to be accessible on the robots file because users of the website can still get to it. Though in this particular website example, the directory didn't really hold secret information, but Elizabeth needs to make sure that she is careful about what is in the robots file on her website. To secure a directory on a web server you can request a password before a person is able to access it. This would make sure that any user is not able to see/access sensitive information. Additionally, try to have their be a limit to how many password attempts the person has to make the directory even more secure.

Source: https://www.thesitewizard.com/apache/password-protect-directory.shtml

3. Service running on waste port: Having an open port isn't a vulnerability alone but having certain services running on those ports can be. The waste port for Elizabeth's website was open and allowed a hacker to get into the website through a username and password they could figure out purely by brute forcing it. This is a vulnerability because though it takes time for the hacker to find the correct password, it is not impossible as shown in homework 2. To secure this service on the port, I would recommend that Elizabeth has either a limit to how many times a person can enter in a password and username until they are blacklisted from the service or that there is a timeout period for every incorrect password, similar to how iPhones have a timeout for incorrect passwords. Though a timeout wouldn't technically prevent brute forcing the password much, but it would make it almost pointless to try because it would take up so much time to get through every possible password. Additionally, it is important that ports are open for a certain purpose and I could argue that this waste port would be better if Elizabeth would just close the port entirely to make her website more secure. 

Source: https://www.networkworld.com/article/3191513/network-security/securing-risky-network-ports.html

** Not sure if #2 really counts so doing one more just in case...

4. Sanitize Source Code: On the website's source code there was a flag and while this flag isn't a real vulnerability, it could be if this was sensitive information. In this way, it is important for Elizabeth to make sure that no sensitive information is included in the source code because this could hurt the integrity of her bank website and lead to a vulnerability.

Source: https://en.wikipedia.org/wiki/HTML_sanitization
