nota1 = float(input ("digite sua primeira nota:"))
nota2 = float(input ("digite sua segundo nota:"))
nota3 = float(input ("digite sua trezera nota:"))
media = (nota1+nota2+nota3)/3 

print (f"sua media é {media}")
if media < 5:
    print("reprovado")
elif media < 10:
    print ("aprovado")
else:
    print ("nota perfeita")
