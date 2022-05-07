import string

_letters=string.ascii_lowercase

def alphabet_caeser_cipher(alphabet,p):
    D={' ':' '}
    n=len(alphabet)
    for i in range(n):
        D[alphabet[i]]=alphabet[i-p]
    return D
#we choose p=4
#print(alphabet_caeser_cipher(_letters,4))


# we create a function that encrypts a text
import re
regex = re.compile('[^a-zA-Z]')

def encryptPlaintext(text,alphabet_caeser_cipher,alphabet,p):
    D=alphabet_caeser_cipher(alphabet,p)
    text=text.rstrip().lower()
    text = regex.sub(' ', text)
    cipherText=[]
    for i in text:
        i=i.lower()
        cipherText.append(D[i])
    return ''.join(cipherText)
print(encryptPlaintext("Ahlem",alphabet_caeser_cipher,_letters,4))

#we get the text using scraping
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

#we do the ecrypting
#print(encryptPlaintext(text,alphabet_caeser_cipher,_letters,4))