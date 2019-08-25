# 3% para o Sindicato 
# FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#	Desconto do IR:
#	Salário Bruto até 900 (inclusive) - isento
#	Salário Bruto até 1500 (inclusive) - desconto de 5%
#	Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Shora= float(input("Digite quanto você ganha por hora de trabalho: "))
Smensal= float(input("Digite quantas horas você trabalha por mês: "))
SBruto= Shora*Smensal
SBruto3= (SBruto*3)/100
SBruto11= (SBruto*11)/100
SBruto5= (SBruto*5)/100
SBruto10= (SBruto*10)/100
SBruto20= (SBruto*20)/100
print("="*100)
if SBruto <= 900:
    print("      Salário Bruto:", "(", Shora, "*", Smensal, ")", "       :  R$", SBruto)
    print("(-)   IR  (0%)                                                :  R$", "00.0")
    print("(-)   INSS (3%)                                               :  R$", SBruto3)
    print("      FGTS (11%)                                              :  R$", SBruto11)
    print("      Total de Descontos                                      :  R$", SBruto3)
    print("      Sálario Liquído                                         :  R$", SBruto-SBruto3)

elif SBruto > 900 and SBruto <= 1500:
    print("      Salário Bruto:", "(", Shora, "*", Smensal, ")", "       :  R$", SBruto)
    print("(-)   IR  (5%)                                                :  R$", SBruto5)
    print("(-)   INSS (3%)                                               :  R$", SBruto3)
    print("      FGTS (11%)                                              :  R$", SBruto11)
    print("      Total de Descontos                                      :  R$", SBruto5+SBruto3)
    print("      Sálario Liquído                                         :  R$", SBruto-SBruto3-SBruto5)

elif SBruto > 1500 and SBruto <= 2500:
    print("      Salário Bruto:", "(", Shora, "*", Smensal, ")", "       :  R$", SBruto)
    print("(-)   IR  (10%)                                                :  R$", SBruto10)
    print("(-)   INSS (3%)                                               :  R$", SBruto3)
    print("      FGTS (11%)                                              :  R$", SBruto11)
    print("      Total de Descontos                                      :  R$", SBruto10+SBruto3)
    print("      Sálario Liquído                                         :  R$", SBruto-SBruto3-SBruto10)

else:
    print("      Salário Bruto:", "(", Shora, "*", Smensal, ")", "       :  R$", SBruto)
    print("(-)   IR  (20%)                                                : R$", SBruto20)
    print("(-)   INSS (3%)                                               :  R$", SBruto3)
    print("      FGTS (11%)                                              :  R$", SBruto11)
    print("      Total de Descontos                                      :  R$", SBruto20+SBruto3)
    print("      Sálario Liquído                                         :  R$", SBruto-SBruto3-SBruto20)