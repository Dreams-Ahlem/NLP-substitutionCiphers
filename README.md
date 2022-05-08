# NLP-substitutionCiphers
 This is a work giving different python algorithms for encrypting and decrypting a plain text.
 
 
 In order to encrypt a text sequence, we use substitution ciphers that aim to replace characters by others. This technique helps to create a map that relates each letter to a specific key to get an encoded text.

There are many ways to perform this encryption and in what follows I will detail some algorithms describing three methods of encrypting:

    Reverse alphabet.
    Caeser cipher.
    Bacon's code.

In this article we have three steps to apply in each method:  First we will create the model that create a dictionary containing  each letter of the alphabet and its code (or value) using one of the three methods listed above. 

Second I will create an algorithm that performs the encryption of a text using the method mentioned. Third get a text from scraping a web site and test the code on it.

Reverse Alphabet:
The substitution applied on this method uses alphabet back-ends so that "a"  becomes "z", "b" becomes "y"   and so on.
    
    ![1](https://user-images.githubusercontent.com/74646377/167289416-1c6d81f2-f07d-4862-b08d-d0753f27519f.png)


Now we will create an algorithm that changes a plain text to an encrypted text using this technique.

To apply this function on a text we need first to remove all the trailing whitespaces and return a copy of the text in lowercase using "rstrip().lower()" and we need, as well, a regular expression regex that is a sequence of characters to specify a search pattern in the text.

    
      ![2](https://user-images.githubusercontent.com/74646377/167289173-0ff70438-d923-42f9-9ae8-c52a7c0f5bee.png)


      

      

      

      


  


