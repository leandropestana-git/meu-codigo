idade = int(input("digite sua idade: "))
experiencianaarea = bool(input("tem experiencia na area: "))
antecedentescriminais =bool(input("possui antecedentes criminais: "))
ensinosuperior = bool(input("ensino superior completo: "))
indição = bool(input("indicado por alguem da emperesa:? "))

if idade > 18 and experiencianaarea and not antecedentescriminais :
    print("venha para uma entrevista")
elif idade >18 and ensinosuperior or indição and not antecedentescriminais:    
    print("venha para uma entrevista")
else :
    print("não venha para entrevista")   
 
