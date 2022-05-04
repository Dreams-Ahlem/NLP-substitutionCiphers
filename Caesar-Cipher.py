 #Replace every letter with the letter 3 before it for a more complex cipher. 
 # Just writing the alphabet backwards for your cipher is pretty simple and will 
 # be easy to crack. If you’d like a more complex cipher, replace every letter 
 # with the letter that comes 3 before it in the alphabet.
#As an easy example, using this cipher, the word "CAT" reads "ZYQ."







import re
import requests
import string
from bs4 import BeautifulSoup


_letters=string.ascii_lowercase

def alphabet_reverse(alphabet):
    dictio={}
    n=len(alphabet)
    for i in range(n):
        dictio[alphabet[i]]=alphabet[n-1-i]
        
    return dictio
dictionary=alphabet_reverse(_letters)

url='https://en.wikipedia.org/w/api.php'
params={'action':'parse','page':'Natural Language Processing', 'format':'json', 'prop':'text','redirects':''}
result=requests.get(url,params=params)
data=result.json()
data #a json file
raw_html=data['parse']['text']['*']#we cannot deal with the result without the soup method
soup=BeautifulSoup(raw_html,'html.parser')#using the soup we can parse the html code
text=''#create a string called text
for p in soup.find_all('p'):#parse the html code between 'p' and transform it to a text 
    text+=p.text#make the text in the text
############################################################################################################################
regex = re.compile('[^a-zA-Z]')
def coding_text(text,dictionary):
    text=text.rstrip().lower()
    #text=text.translate(str.maketrans('','',string.punctuation))
    text = regex.sub(' ', text)
    coded_message=[]
    for ch in text:
        value=ch
        if ch in dictionary:
            value=dictionary[ch]
        coded_message.append(value)
    return ''.join(coded_message)
    
        
        
    
code=coding_text(text,dictionary)
code
#############################################################################################################################

def decoding_cipher(cipherText,dictionary):
    decoded_message=[]
    for ch in cipherText:
        value=ch
        if ch in dictionary:
            value=dictionary[ch]
        decoded_message.append(value)
    return ''.join(decoded_message)



