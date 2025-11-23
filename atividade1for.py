nomedalista = ["davi barbosa","davi gerso","diogo verissimo","leandro vieira","liam de castro"]
print ("nome do aluno "+str(nomedalista))
numerodalista = int(input("digite o indicio do aluno "))
if numerodalista >= 5:
    print ( "numero maior que a lista ")
elif numerodalista <= -1:
    print ( "numero menor que a lista ")
else:
    print (nomedalista[numerodalista])
