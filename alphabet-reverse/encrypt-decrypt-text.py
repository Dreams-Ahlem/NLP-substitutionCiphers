
import string
import re



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
#The encrypting part:
import re
regex = re.compile('[^a-zA-Z]')

def encryptPlaintext(text,alphabet_reverse,alphabet):
    D=alphabet_reverse(alphabet)
    text=text.rstrip().lower()
    text = regex.sub(' ', text)
    cipherText=[]
    for i in text:
        i=i.lower()
        cipherText.append(D[i])
    return ''.join(cipherText)
encryptPlaintext("Ahlem",alphabet_reverse,_letters)

#We will get the text fro scraping a website 
import requests
from bs4 import BeautifulSoup
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
text

def decryptCyphertext(text,alphabet_reverse,alphabet):
    D=alphabet_reverse(alphabet)
    plainText=[]
    for i in text:
        i=i.lower()
        position=list(D.values()).index(i)
        plainText.append(list(D.keys())[position])
    return ''.join(plainText)

