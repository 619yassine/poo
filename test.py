

import random 
from random import choice
import string
import array


import unicodedata
import itertools
import datetime
def leet(txt):
    sortie=""  
    for c in txt.upper():
        if c=="A":
            sortie+="4"
        elif c=="E":
            sortie+="3"
        elif c=="I":
            sortie+="1"
        elif c=="O":
            sortie+="0"
        else:
            sortie+=c
    return sortie
    

class date:
    def __init__(self,date):
        self.__jour = date.split("/")[0]
        self.__mois = date.split("/")[1]
        self.__annee = date.split("/")[2]
    def melangeurdate(self):
        array = []
        array.append(self.__jour)
        array.append(self.__mois)
        array.append(self.__annee)
        array.append(self.__jour+self.__annee)
        array.append(self.__mois+self.__annee)
        array.append(self.__jour+self.__mois)
        array.append(self.__jour+self.__mois+self.__annee)
        return(array)
class mot:
    def __init__(self,nom,prenom):
        self.__nom = nom
        self.__prenom = prenom
    
    def melangeurnom(self):
        array = []
        array.append(self.__nom.upper())
        array.append(self.__nom.lower())
        array.append(self.__nom.title())
        array.append(leet(self.__nom))
        array.append(leet(self.__nom).lower())
        return(array)
    def melangeurprenom(self):
        array = []
        array.append(self.__prenom.upper())
        array.append(self.__prenom.lower())
        array.append(self.__prenom.title())
        array.append(leet(self.__prenom))
        array.append(leet(self.__prenom).lower())
        return(array)
        #res = ''.join(choice((str.upper, str.lower))(char) for char in pwd)    
        #with open(r"C:\Users\000208799\Desktop\monfichier.txt", "w") as file:
        #    file.write(res)
#class mdp(mot,date):
#    def __init__(self,date[],mot[]):
 #       for i in range(len(date)):
  #          self.__date[i] = date[i]
   #     for i in range(len(mot)):
    #        self.__mot[i] = mot[i]
    #
    #def password(self):
     #   for i in range(len(self.__date)):

    

tabm = "yassine"  
tabd = "19/07/1999"         
test = mot("yassine","khattabi")
test2 = date(tabd)
mnom = test.melangeurnom()
mpnom = test.melangeurprenom()
mdate = test2.melangeurdate()
abc = [mnom,mpnom,mdate]
acb = [mnom,mdate,mpnom]
bac = [mpnom,mnom,mdate]
bca = [mpnom,mdate,mnom]
cba = [mdate,mpnom,mnom] 
cab = [mdate,mnom,mpnom]

#res = list(itertools.product(*abc))
#res.append(list(itertools.product(*abc)))
res = (list(itertools.product(*acb)))
res += (list(itertools.product(*bac)))
res += (list(itertools.product(*bca)))
res += (list(itertools.product(*cba)))
res += (list(itertools.product(*cab)))
print(res)