# Writeup 7 - Binaries I

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main() {
	b = 0x1ceb00da;
	a = 0xfeedface;

	printf("a = %d\n", a);
	printf("b = %d\n", b);

	//xor stuff
	a ^= b;
	b ^= a;
	a ^= b;

	printf("a = %d\n", a);
	printf("b = %d\n", b);

	return 0;
}
```

### Part 2 (10 Pts)

This program holds two numbers in variables that I am calling a and b and then uses XOR to switch the value of a to b and b to a. 
