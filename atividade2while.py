import random
max =int (input("adivinha ate que numero "))
chances = int (input("quanta chances "))
escolhernumero = 0
numerosecreto =  random.randint(1,max)
while chances >0: 
    chances = chances -1
    escolhernumero = int(input ("vamos escolher enter 1 e max: "))
    if escolhernumero < numerosecreto:
        print ("numero menor errado,tente numero maior")
    elif escolhernumero > numerosecreto:
        print ("numero maior errado,tente numero menor")
    else:
        print ("acertou")
        chances = 0
    
