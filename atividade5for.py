listaperguntas = ["quantos dias tem um ano","quantas pessoas tem no canada","quantos gêneros de macaco tem na africa"]
listarespostas = ["365","41,7 mihoes","164"]
quantoacertou = 0
for i in range (3):
    print (listaperguntas[i])
    respostapessoa = input("escreva sua resposta: ")

    if listarespostas [i] == respostapessoa :
        print ("jogador acertou")
        quantoacertou +=1
    elif respostapessoa == "" :
        print ("não escreveu nada")
    else:
        print ("resposta erroda")


print ("acertou "+ str(quantoacertou))
