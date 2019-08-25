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