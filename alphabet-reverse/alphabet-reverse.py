# Reverse the alphabet to create a basic cipher alphabet. Substitution ciphers 
#work by creating a disordered alphabet, allowing you to substitute letters for 
#other letters. For a straightforward substitution cipher, simply use the alphabet
#backwards, so that "a" becomes "z," "b" becomes "y," "c" becomes "x," and 
#so on.

#This substitution cipher would read: ZYXWVUTSRQPONMLKJIHGFEDCBA.
#This second alphabet is often referred to as the "ciphertext."
import string


# We assign to _letters the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.

_letters=string.ascii_lowercase

def alphabet_reverse(alphabets):
    #This function will create a dictionary that assigns to each letter of the alphabet 
    #its value= an alphabet back-end
    D={' ':' '} #we create an dictionary containing the space and its value
    n=len(alphabets)
    for i in range(n):
        D[alphabets[i]]=alphabets[n-1-i]
    return D
dictionary=alphabet_reverse(_letters)


print(dictionary)



