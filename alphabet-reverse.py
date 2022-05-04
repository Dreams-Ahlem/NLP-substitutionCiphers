# Reverse the alphabet to create a basic cipher alphabet. Substitution ciphers 
#work by creating a disordered alphabet, allowing you to substitute letters for 
#other letters. For a straightforward substitution cipher, simply use the alphabet
#backwards, so that "a" becomes "z," "b" becomes "y," "c" becomes "x," and 
#so on.

#This substitution cipher would read: ZYXWVUTSRQPONMLKJIHGFEDCBA.
#This second alphabet is often referred to as the "ciphertext."




import string


_letters=string.ascii_lowercase

def alphabet_reverse(alphabet):
    dictio={}
    n=len(alphabet)
    for i in range(n):
        dictio[alphabet[i]]=alphabet[n-1-i]
        
    return dictio
dictionary=alphabet_reverse(_letters)



