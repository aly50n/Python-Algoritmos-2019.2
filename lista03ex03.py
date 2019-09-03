print("O país A tem 80 mil habitantes com um crescimento de 3 porcento ao ano")
print("O país B tem 20000 habitantes com um crescimento de 1.5 porcento ao ano.")
paisA = 80000 
paisB = 200000
cont = 0
while paisA < paisB:
    contaA = (paisA * 3) / 100
    contaB = (paisB * 1.5) / 100
    paisA = contaA + paisA
    paisB = contaB + paisB
    cont = cont + 1
    if paisA == paisB:
        print ("O país A em", cont, "anos terá a mesma quantidade de habitantes que o país B.")
    if paisA > paisB:
        print ("O país A em", cont, "anos terá um número maior de habitantes que o país B.")