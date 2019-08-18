print("Seja bem-vindo ao calculador de Área em M² de uma casa de até 04 cômodos")
print("Por favor insira a Largura e o Comprimento em Metros² de cada comodo a seguir:")
print("Obs: Caso sua casa tenha menos de 04 cômodos coloque o valor de -> 0 <- nos cômodos que não existem e dê enter.")

l1=float(input("Qual a LARGURA DO CÔMODO 01? "))
c1=float(input("Qual o COMPRIMENTO DO CÔMODO 01? "))
a1=float(l1*c1)
print("A Área do Cômodo 01 é de->", a1, "M²")

l2=float(input("LARGURA DO CÔMODO 02-> "))
c2=float(input("COMPRIMENTO DO CÔMODO 02-> "))
a2=float(l2*c2)
print("A Área do Cômodo 02 é de->", a2, "M²")

l3=float(input("LARGURA DO CÔMODO 03-> "))
c3=float(input("COMPRIMENTO DO CÔMODO 03-> "))
a3=float(l3*c3)
print("A Área do Cômodo 03 é de->", a3, "M²")

l4=float(input("LARGURA DO CÔMODO 04-> "))
c4=float(input("COMPRIMENTO DO CÔMODO 04-> "))
a4=float(l4*c4)
print("A Área do Cômodo 04 é de->", a4, "M²")

atotal=float(a1+a2+a3+a4)
print("A ÁREA TOTAL DA SUA CASA É DE:", atotal, "M²")