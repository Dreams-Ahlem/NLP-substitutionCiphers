import string

_letters=string.ascii_lowercase
def bacon_s_code(alphabet):
    dict={' ':' '}
    ##############################
    L=[]
    for i in range(0,5):
        L.append(10**i)
        for j in range(0,len(L)-1):
            L.append(10**i+L[j])
    ############################
    l=['00000']
    for i in L[:23]:
        s=''
        for j in range(5-len(str(i))):
            s+='0'
        s+=str(i)
        l.append(s)
    ###################################3
    liste=[]
    for i in l:
        for x in i:
            if x=='0':
                i=i.replace(x[0],'A')
            if x=='1':
                i=i.replace(x[0],'B')
        liste.append(i)
    ################################3
    for i in range(8):
        dict[alphabet[i]]=liste[i]
    for i in range(8,9):
        dict[alphabet[i]],dict[alphabet[i+1]]=liste[i],liste[i]
    for i in range(10,20):
            dict[alphabet[i]]=liste[i-1]
    for i in range(20,21):
        dict[alphabet[i]],dict[alphabet[i+1]]=liste[i-1],liste[i-1]
    for i in range(22,26):
        dict[alphabet[i]]=liste[i-2]
    return dict
bacon_s_code(_letters)