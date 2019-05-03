# Crypto II Writeup

Name: Erin Schick
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Erin Schick

## Assignment Writeup

### Part 1 (70 Pts)

Did the following commands:
gpg --import key.asc
gpg ----decrypt message.txt.gpg

Flag that I got: CMSC389R-{m3ss@g3_!n_A_b0ttl3}


### Part 2 (30 Pts)

Both of these pictures seemed to be decrypted pixel by pixel. In the ecb photo you can still see the oval and rectangle that were in the original picture where as in the cbc photo you cannot see them at all. This would lead me to think that the cbc encyption is more secure than the ecb encryption because in the ecb encryption there was a leak of information. While ecb just uses the same key to encrypt one block of the cipher and this process is the same for each block, the output is very determinate which leads to the leak of information. CBC however uses the encrypted block from the previous block as an extra key that the message is XORed by before it is encrypted with the key. This makes the process a lot less determinate and therefore more secure. 