escolhernumero = 0
numerosecreto =  5
while numerosecreto != escolhernumero:
    escolhernumero = int(input ("vamos escolher enter 1 e 10: "))
    if escolhernumero < numerosecreto:
        print ("numero menor errado,tente numero maior")
    elif escolhernumero > numerosecreto:
        print ("numero maior errado,tente numero menor")
    else:
        print ("acertou")
    
