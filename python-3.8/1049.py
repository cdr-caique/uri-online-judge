import os

str1 = str(input())
str2 = str(input())
str3 = str(input())

if(str1 == "vertebrado"):
    if(str2 == "ave"):
        if(str3 == "carnivoro"):
            print("aguia")
            os.system("exit")
        if(str3 == "onivoro"):
            print("pomba")
            os.system("exit")
    if(str2 == "mamifero"):
        if(str3 == "onivoro"):
            print("homem")
            os.system("exit")
        if(str3 == "herbivoro"):
            print("vaca")
            os.system("exit")
if(str1 == "invertebrado"):
    if(str2 == "inseto"):
        if(str3 == "hematofago"):
            print("pulga")
            os.system("exit")
        if(str3 == "herbivoro"):
            print("lagarta")
            os.system("exit")
    if(str2 == "anelideo"):
        if(str3 == "hematofago"):
            print("sanguessuga")
            os.system("exit")
        if(str3 == "onivoro"):
            print("minhoca")
            os.system("exit")
