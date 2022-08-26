import random

# itse peli
def muuttuja():
    peli = True
    vastaus = random.randint(1,50)
    while peli:
	    arvaus = int(input())
	    if arvaus > vastaus:
		    print("Luku on pienempi")
	    elif arvaus < vastaus:
		    print("Luku on suurempi")
	    else:
		    print("Oikein arvattu")
		    peli = False

# pelin aloitus
print("*" * 50)
print("Tervetuloa numeropeliin!") 
print("*" * 50)
while int(input("Haluatko pelata ei=0 kyllä=1: ")):
    print("Anna luku.")
    muuttuja()
