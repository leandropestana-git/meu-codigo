idade = int(input("digite sua idade: "))
ingresso = bool(input("tem ingresso? "))
autorizaçaodospais = bool(input("tem autorizaçao dos pais? "))
listavip = bool(input("entrar mesmo sem ingresso? "))
if idade >=18 and  (ingresso or vip):
  print ("pode entrar")
elif idade <12 :
print ("nao pode entrar ") 
elif idade <18 and autorizaçaodospais and (ingresso or vip) :
  print (" pode entrar ")
else :
  print ("nao pode entrar ") 
