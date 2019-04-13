/*
 * Name: Erin Schick
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Erin Schick
 */

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
