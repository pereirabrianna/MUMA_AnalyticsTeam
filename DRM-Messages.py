'''
This python code is meant to receive an encrypted message
and after splitting the message in half (Divide), summing up the
alphabet index values of each half and shifting them by the
calculated value (Rotate), and finally shifting each character
in the first half by the index value of the corresponding character
in the second half (Merge) will it decrypt the message.

'''

# this function shifts the letters in the string by the specified amount
def cipher(strin,shift):
    moved = ""
    for ch in strin:
        moved += chr((ord(ch)+shift-65) % 26+65)
    return moved

import string
import sys

# receiving input as string
x = str(input())

# creating an uppercase list of the alphabet
alphabet = []
alphabet = list(string.ascii_uppercase)

rotate1 = 0
rotate2 = 0
rotated_string1 = ""
rotated_string2 = ""
merge_shifts = []
merge_string = ""
count = 0

# splits the input string in half
divide1 = x[0:len(x)//2]
divide2 = x[len(x)//2:]

# calculates the rotation value for the two new strings
for i in divide1:
    for j in alphabet:
        if i == j:
            rotate1 += alphabet.index(j)
for k in divide2:
    for l in alphabet:
        if k == l:
            rotate2 += alphabet.index(l)

# calls upon the function above to shift each string by its rotation value
rotated_string1 = cipher(divide1,rotate1)
rotated_string2 = cipher(divide2,rotate2)

# places the index value of each character in the second string into a list
for ar in rotated_string2:
    for ac in alphabet:
        if ar == ac:
            merge_shifts.append(alphabet.index(ac))
            
# shifts each character in the first string by the value from the second string            
for ter in rotated_string:
    merge_string += chr((ord(ter)+merge_shifts[count]-65) % 26+65)
    count += 1

# prints the decrypted message    
print(merge_string)


