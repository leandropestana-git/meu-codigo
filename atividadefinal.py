vidadepaladino = 10
vidadomonstro = 10
curar = 1
raio =1
for i in range (4):
    print(" vida paladino: "+ str (vidadepaladino)+" vida monstro: "+ str (vidadomonstro))
    print("quantas rodadas: "+ str (4-i))
    acao = input("qual acao (espada,cura,raio)? ")

    if acao == "espada":
        vidadomonstro -=3
    elif acao == "cura" and curar==1:
        vidadepaladino +=6
        curar =0
    elif acao == "raio" and raio==1:
        vidadomonstro -=6
        raio =0

    if vidadomonstro <=0:
        print("voce vence")
        break

    if vidadepaladino <=0:
        print("voce perdeu")
        break

    print("o monstro atacou")
    vidadepaladino -=5
          
